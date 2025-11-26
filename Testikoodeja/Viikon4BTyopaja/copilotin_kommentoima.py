
"""
Read and process reservation data.

This module provides helper functions to:
- parse raw reservation records from a text file,
- print summaries (confirmed reservations, long reservations, status list),
- compute counts and total revenue for confirmed reservations.

Input format expectation:
Each reservation line in the file is a single record whose fields are separated
by newline characters (split with '\n'), in the following order:

    [0] varausId (int, as string)
    [1] nimi (str)
    [2] sähköposti (str)
    [3] puhelin (str)
    [4] varauksenPvm (date as "YYYY-MM-DD")
    [5] varauksenKlo (time as "HH:MM")
    [6] varauksenKesto (int, hours)
    [7] hinta (float, price per hour)
    [8] varausVahvistettu ("true"/"false")
    [9] varattuTila (str, room/space name)
    [10] varausLuotu (datetime as "YYYY-MM-DD HH:MM:SS")

Note: The first element of the `varaukset` list is a header row.
"""

from __future__ import annotations

from datetime import datetime, date, time
from typing import List, Any


def muunna_varaustiedot(varaus: List[str]) -> List[Any]:
    """
    Convert a raw reservation field list (strings) into typed values.

    Parameters
    ----------
    varaus : List[str]
        A list of 11 string fields representing a single reservation:
        [varausId, nimi, sähköposti, puhelin, varauksenPvm, varauksenKlo,
         varauksenKesto, hinta, varausVahvistettu, varattuTila, varausLuotu]

    Returns
    -------
    List[Any]
        A list with parsed types:
        [int, str, str, str, date, time, int, float, bool, str, datetime]
    """
    muutettu_varaus: List[Any] = []

    # Parse ID
    muutettu_varaus.append(int(varaus[0]))

    # Basic strings
    muutettu_varaus.append(varaus[1])  # nimi
    muutettu_varaus.append(varaus[2])  # sähköposti
    muutettu_varaus.append(varaus[3])  # puhelin

    # Dates and times
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())

    # Duration (hours) and price per hour
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))

    # Confirmation flag ("true"/"false" → bool)
    muutettu_varaus.append(varaus[8].lower() == "true")

    # Room/space
    muutettu_varaus.append(varaus[9])

    # Creation timestamp
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))

    return muutettu_varaus


def hae_varaukset(varaustiedosto: str) -> List[List[Any]]:
    """
    Read reservations from a text file and return a list including a header row.

    Parameters
    ----------
    varaustiedosto : str
        Path to the reservation file. Each line is a single reservation record
        whose fields are separated by newline characters.

    Returns
    -------
    List[List[Any]]
        The first item is a header list (column names).
        Subsequent items are reservation rows produced by `muunna_varaustiedot`.
    """
    varaukset: List[List[Any]] = []

    # Header row describing column names
    varaukset.append(
        [
            "varausId",
            "nimi",
            "sähköposti",
            "puhelin",
            "varauksenPvm",
            "varauksenKlo",
            "varauksenKesto",
            "hinta",
            "varausVahvistettu",
            "varattuTila",
            "varausLuotu",
        ]
    )

    # Read file line by line
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            # Remove trailing newline from the record
            varaus = varaus.strip()

            # Split fields by newline characters within the record
            varaustiedot = varaus.split("\n")

            # Convert to typed fields and append
            varaukset.append(muunna_varaustiedot(varaustiedot))

    return varaukset


def vahvistetut_varaukset(varaukset: List[List[Any]]) -> None:
    """
    Print a formatted list of confirmed reservations.

    Parameters
    ----------
    varaukset : List[List[Any]]
        A list containing a header row at index 0 and reservation rows after it.
    """
    # Skip the header row at index 0
    for varaus in varaukset[1:]:
        if varaus[8]:
            # Example: "- Matti Meikäläinen, Room A, 01.02.2025 klo 09.30"
            print(
                f"- {varaus[1]}, {varaus[9]}, "
                f"{varaus[4].strftime('%d.%m.%Y')} klo {varaus[5].strftime('%H.%M')}"
            )
    print()  # trailing blank line for readability


def pitkat_varaukset(varaukset: List[List[Any]]) -> None:
    """
    Print reservations whose duration is at least 3 hours.

    Parameters
    ----------
    varaukset : List[List[Any]]
        A list containing a header row at index 0 and reservation rows after it.
    """
    for varaus in varaukset[1:]:
        if varaus[6] >= 3:
            print(
                f"- {varaus[1]}, {varaus[4].strftime('%d.%m.%Y')} "
                f"klo {varaus[5].strftime('%H.%M')}, "
                f"kesto {varaus[6]} h, {varaus[9]}"
            )
    print()


def varausten_vahvistusstatus(varaukset: List[List[Any]]) -> None:
    """
    Print a status line per reservation indicating confirmation.

    Parameters
    ----------
    varaukset : List[List[Any]]
        A list containing a header row at index 0 and reservation rows after it.
    """
    for varaus in varaukset[1:]:
        if varaus[8]:
            print(f"{varaus[1]} → Vahvistettu")
        else:
            print(f"{varaus[1]} → EI vahvistettu")
    print()


def varausten_lkm(varaukset: List[List[Any]]) -> None:
    """
    Print counts for confirmed and unconfirmed reservations.

    Parameters
    ----------
    varaukset : List[List[Any]]
        A list containing a header row at index 0 and reservation rows after it.
    """
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0

    for varaus in varaukset[1:]:
        if varaus[8]:
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl")
    print()


def varausten_kokonaistulot(varaukset: List[List[Any]]) -> None:
    """
    Compute and print total revenue from confirmed reservations.

    Revenue is calculated as `varauksenKesto * hinta` for each confirmed reservation.

    Parameters
    ----------
    varaukset : List[List[Any]]
        A list containing a header row at index 0 and reservation rows after it.
    """
    varaustenTulot = 0.0

    for varaus in varaukset[1:]:
        if varaus[8]:
            varaustenTulot += varaus[6] * varaus[7]

    # Use comma as decimal separator for output formatting
    print(
        "Vahvistettujen varausten kokonaistulot:",
        f"{varaustenTulot:.2f}".replace(".", ","),
        "€",
    )
    print()


def main() -> None:
    """
    Entry point: read reservations and print all reports.
    """
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)

    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)

    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)


if __name__ == "__main__":
    main()
