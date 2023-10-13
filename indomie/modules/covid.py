# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from covid import Covid
from indomie import CMD_HELP
from indomie.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Terdeteksi   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif      : {country_data['active']}`\n"
        output_text += f"`🤕mau mati    : {country_data['critical']}`\n"
        output_text += f"`😟baru banget mati  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️dah mati mek      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔kasus baru   : {country_data['new_cases']}`\n"
        output_text += f"`😇Alhamdulillah   : {country_data['recovered']}`\n"
        output_text += f"`🧪Total tests : {country_data['total_tests']}`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")


@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Terkonfirmasi   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif      : {country_data['active']}`\n"
        output_text += f"`🤕Kritis    : {country_data['critical']}`\n"
        output_text += f"`😟Kematian Baru  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Mati      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔Kasus Baru   : {country_data['new_cases']}`\n"
        output_text += f"`😇Sembuh   : {country_data['recovered']}`\n"
        output_text += "`🧪Total tests : N/A`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"`Corona Virus Info in {country}:`\n\n{output_text}")


CMD_HELP.update({"covid": "`.covid `**<country>**"
                 "\n`Usage: Get an information about covid-19 data in your country.`\n\n"
                 "`.covid`"
                 "\n`Usage: Get an information about covid-19 data in Worldwide.`\n"})
