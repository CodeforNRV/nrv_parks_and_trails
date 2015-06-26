import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open("nrv-parks-and-trails-739f81b49ac1.json"))
scope = ["https://spreadsheets.google.com/feeds"]
google_sheet_url = "https://docs.google.com/spreadsheets/d/15-60RpIqkM2nev4S0UNt7h5M5mhuvegPFO8X-TU8rKg"

credentials = SignedJwtAssertionCredentials(json_key["client_email"], json_key["private_key"], scope)

#if this line doesn't work, look at the wiki for python install instructions
gc = gspread.authorize(credentials)

#url not found? not sure why
sheet = gc.open_by_url(google_sheet_url)
