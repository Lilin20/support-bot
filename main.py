import discord
from discord.ext import commands
import os
import configparser
import random

c_parser = configparser.ConfigParser()
c_parser.read(os.path.dirname(os.path.realpath(__file__))+"/config.ini")

# Object
bot = discord.Bot()

# Event - Startup
@bot.event
async def on_ready():
    print("Ready")
    bot.add_view(SupportView())
    bot.add_view(RoleSelectionView())

### START OF SUPPORT SECTION ###
class SupportView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Support-Ticket", custom_id="ticket_button", style=discord.ButtonStyle.primary, emoji="🎫")
    async def first_button_callback(self, button, interaction):
        modal = SupportModal(title="Support-Ticket")
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Channel Request", custom_id="channelreq_button", style=discord.ButtonStyle.primary, emoji="📝")
    async def second_button_callback(self, button, interaction):
        modal = ChannelReqModal(title="Channel Request")
        await interaction.response.send_modal(modal)

class CloseButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Ticket schließen", custom_id="close_button", style=discord.ButtonStyle.secondary, emoji="❌")
    async def close_button_callback(self, button, interaction):
        await interaction.channel.delete()

class ChannelReqModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Channel Name"))
        self.add_item(discord.ui.InputText(label="Channel Typ (Text/Voice)"))
        self.guild = bot.get_guild(646454347676254228)
        self.category = discord.utils.get(self.guild.categories, id=1117833172718190663)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Channel Request created!", ephemeral=True, delete_after=5)
        member = interaction.user
        overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)
        }
        channel = await self.guild.create_text_channel(name=f"channel-request#{random.randint(0, 10000)}", category=self.category, overwrites=overwrites)
        await channel.send(f"{member.mention} hat einen Channel-Request erstellt!\n\n**Channel Name:** {self.children[0].value}\n**Channel Typ:** {self.children[1].value}", view=CloseButtons())

class SupportModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(discord.ui.InputText(label="Anliegen"))
        self.add_item(discord.ui.InputText(label="Kateogrie (Beleidigung, Bug, etc.)"))
        self.add_item(discord.ui.InputText(label="Betroffene Personen"))
        self.add_item(discord.ui.InputText(label="Beschreibung", style=discord.InputTextStyle.long))
        self.guild = bot.get_guild(646454347676254228)
        self.category = discord.utils.get(self.guild.categories, id=1117833172718190663)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Support-Ticket created!", ephemeral=True, delete_after=5)
        member = interaction.user
        overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True, read_message_history=True)
        }
        channel = await self.guild.create_text_channel(name=f"support-ticket#{random.randint(0, 10000)}", category=self.category, overwrites=overwrites)
        await channel.send(f"{member.mention} hat ein Support-Ticket erstellt!\n\n**Anliegen:** {self.children[0].value}\n**Kategorie:** {self.children[1].value}\n**Betroffene Personen:** {self.children[2].value}\n**Beschreibung:** {self.children[3].value}", view=CloseButtons())
### END OF SUPPORT SECTION ###

### START OF ROLE SELECTION SECTION ###
class RoleSelectionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        placeholder = "Wähle deine Rolle aus (nur ITF Klassen)",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label = "ITF22a",
                description = "Schüler der Klasse ITF22a"
            ),
            discord.SelectOption(
                label = "ITF22b",
                description = "Schüler der Klasse ITF22b"
            ),
            discord.SelectOption(
                label = "ITF22c",
                description = "Schüler der Klasse ITF22c"
            ),
            discord.SelectOption(
                label = "ITF22d",
                description = "Schüler der Klasse ITF22d"
            ),
            discord.SelectOption(
                label = "ITF22e",
                description = "Schüler der Klasse ITF22e"
            )
        ]
    , custom_id="role_selection_itf")
    async def ITFrole_selection_callback(self, select, interaction):
        member = interaction.user
        role = discord.utils.get(member.guild.roles, name=select.values[0])
        schüler_role = discord.utils.get(member.guild.roles, name="Schüler")
        itf_role = discord.utils.get(member.guild.roles, name="ITF")
        for r in member.roles:
            if r.name != "@everyone":
                await member.remove_roles(r)
        await member.add_roles(role)
        await member.add_roles(schüler_role)
        await member.add_roles(itf_role)
        self.children[0].disabled = True
        self.children[1].disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"Du hast die Rolle {role.mention} erhalten!", ephemeral=True, delete_after=5)

    @discord.ui.select(
        placeholder = "Wähle deine Rolle aus (nur ITA Klassen)",
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label = "ITA20",
                description = "Schüler der Klasse ITA20"
            ),
            discord.SelectOption(
                label = "ITA21a",
                description = "Schüler der Klasse ITA21a"
            ),
            discord.SelectOption(
                label = "ITA21b",
                description = "Schüler der Klasse ITA21b"
            ),
            discord.SelectOption(
                label = "ITA22a",
                description = "Schüler der Klasse ITA22a"
            )
        ]
    , custom_id="role_selection_ita")
    async def ITArole_selection_callback(self, select, interaction):
        member = interaction.user
        role = discord.utils.get(member.guild.roles, name=select.values[0])
        schüler_role = discord.utils.get(member.guild.roles, name="Schüler")
        ita_role = discord.utils.get(member.guild.roles, name="ITA")
        for r in member.roles:
            if r.name != "@everyone":
                await member.remove_roles(r)
        await member.add_roles(role)
        await member.add_roles(schüler_role)
        await member.add_roles(ita_role)
        self.children[0].disabled = True
        self.children[1].disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(f"Du hast die Rolle {role.mention} erhalten!", ephemeral=True, delete_after=5)
### END OF ROLE SELECTION SECTION ###

@bot.slash_command(name="create_role_selection", description="Get your class role")
@commands.has_permissions(administrator=True)
async def create_role_selection(ctx):
    embed=discord.Embed(title="Rollen-Selector", description="Mit dem Slash-Befehl /select_role kannst du den Selector aufrufen. Dieser bleibt für 20 Sekunden und veschwindet dann wieder.", color=0x00bd2f)
    embed.add_field(name="Information", value="Falls deine Klasse fehlt erstell bitte ein Support-Ticket! Wir haben nicht alle Klassen aber sind bereit alle Klassen hinzuzufügen!", inline=False)
    embed.set_footer(text="Support-Bot - v0.1")
    await ctx.send(embed=embed)
    await ctx.respond("Success", ephemeral=True, delete_after=5)


@bot.slash_command(name="create_support_embed", description="Get support for the bot")
@commands.has_permissions(administrator=True)
async def create_support_embed(ctx):
    embed=discord.Embed(title="Support / Channel Requests", description="Hier kannst du ein Support-Ticket erstellen oder eine Anfrage zur Erstellung eines Channels stellen.", color=0x00bd2f)
    embed.add_field(name="How-to", value="Drücke den jeweiligen Button für dein Anliegen.", inline=False)
    embed.set_footer(text="Support-Bot - v0.1")
    await ctx.send(embed=embed, view=SupportView())
    await ctx.respond("Success", ephemeral=True, delete_after=5)

@bot.slash_command(name="select_role", description="Ruft den Role-Selector auf")
async def select_role(ctx):
    await ctx.respond(view=RoleSelectionView(), ephemeral=True, delete_after=20)

bot.run(c_parser.get('Bot', 'token'))