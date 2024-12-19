import discord
from discord.ext import commands
from discord import interactions
from discord.utils import MISSING


Intents = discord.Intents.default()
Intents.message_content = True
Intents.members = True

bot = commands.Bot(command_prefix="!", intents=Intents)
trr = bot.tree


@bot.event
async def on_ready():
    await trr.sync()
    print(f"I am ready sir {bot.user}")

class new(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="anithing", style=discord.ButtonStyle.gray)
    async def a(self,interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_modal(wassim_modal())
        
class wassim_modal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="TEST MODAL")
    name = discord.ui.TextInput(
        label='Name',
        placeholder='Enter your name'
    )
    discord_name = discord.ui.TextInput(
        label="your discord name",
        placeholder='Enter your discord Name'
    )
    about = discord.ui.TextInput(
        label="About you",
        placeholder="Enter anithing",
        style=discord.TextStyle.long,
        max_length= 2000,
        required=False
    )
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Thanks or writing {self.name.value} or {self.discord_name.value}")
        
@trr.command(name="tttt", description="anithing")
async def d(interaction: discord.Interaction):
    view = new()
    await interaction.response.send_message(f"hehe", view=view)
