import os
import discord
from dotenv import load_dotenv
from datetime import datetime
import csv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
fname = "memberLogon.csv"

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

def load_member_list():
    members = []
    if os.path.exists(fname):
        with open(fname, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                members.append({"id": int(row["id"]), "join_date": row["join_date"]})
    return members

def save_member_list(members):
    with open(fname, "w", newline="") as csvfile:
        fieldnames = ["id", "join_date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for member in members:
            writer.writerow(member)

@client.event 
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    members = load_member_list()
    print("Loaded Member List:", members)

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")
    members = load_member_list()
    members.append({"id": member.id, "join_date": str(datetime.now())})
    save_member_list(members)
    print("Updated Member List:", members)

    # Greet the new member
    welcome_channel_id = 1179581190865428492
    welcome_channel = member.guild.get_channel(welcome_channel_id)
    if welcome_channel:
        await welcome_channel.send(f"Welcome, {member.mention}! Thanks for joining our server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")
    members = load_member_list()
    members = [m for m in members if m["id"] != member.id]
    save_member_list(members)
    print("Updated Member List:", members)

client.run('MTE3OTU3NDkzNTIxMjAxOTc2Mw.GCQNQx.0_MqVlZFTWyl73keCiTTrFykb8ZYzM1o858eIc')


#server link; https://discord.gg/XE6HQ7xq
