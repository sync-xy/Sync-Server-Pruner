import os

os.system("pip install -U discord.py-self")
os.system('sleep 2 && clear' if 'TERMUX_VERSION' in os.environ else 'sleep 2 && clear >/dev/null 2>&1 &' if os.name == 'posix' else 'timeout /t 2 >nul 2>&1 && cls')

import sys
import discord
import asyncio
from discord.ext import commands

sync = commands.Bot(command_prefix="syncjija", case_insensitive=False, self_bot=True, intents=discord.Intents.all())

def gradient(text, haha, hahaa):
    gradient_length = len(text)
    output = ""
    for i, char in enumerate(text):
        r = int(haha[0] + (hahaa[0] - haha[0]) * (i / gradient_length))
        g = int(haha[1] + (hahaa[1] - haha[1]) * (i / gradient_length))
        b = int(haha[2] + (hahaa[2] - haha[2]) * (i / gradient_length))
        output += f"\033[38;2;{r};{g};{b}m{char}"
    output += "\033[0m"
    return output

def made_by_sync(content_lines, haha, hahaa):
    lul = max(len(line) for line in content_lines)
    hul = "╔" + "═" * (lul + 2) + "╗"
    gul = "╚" + "═" * (lul + 2) + "╝"
    
    draw = [hul]
    for line in content_lines:
        draw.append(f"║ {line.ljust(lul)} ║")
    draw.append(gul)
    
    txt = "\n".join(draw)
    return gradient(txt, haha, hahaa)


art = """
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                
                                                                                
"""


contact = [
    "GitHub - https://github.com/sync-xy",
    "Discord - @01sync | Async Development"
]


print(gradient(art, (128, 0, 255), (0, 255, 255)))  


print(made_by_sync(contact, (128, 0, 255), (0, 255, 255)))

@sync.event
async def on_ready():
    print(f"Connected To :{sync.user}")
    await asyncio.sleep(1.5)
    response = input(f"Are you sure you want to prune server {server_id} (Y/N): ")
    if response.lower() in ('y', 'yes'):
        await sync_prune()
    elif response.lower() in ('n', 'no'):
        print("Exiting.")
        exit()
    else:
        print("Invalid response. Exiting.")
        exit() 

############### CONFIGURATION ###########################
wall_role = False   # if server has wall role if yes then put True if no then put False
wall_role_id = 0      # if no wall role then 0
server_id = 1204457412958879795  # server to prune
token = " Enter Your Token" 
#######################################################

async def sync_prune():
    guild = sync.get_guild(server_id)
    if not guild:
        print("Server not found.")
        return
    
    if not guild.me.guild_permissions.administrator and not guild.me.guild_permissions.kick_members:
        print("Insufficient permissions to prune members.")
        return

    sync_roles = [role for role in guild.roles if len(role.members) != 0]
    reason = "Sync Was Here"
    sync_pruned = await guild.prune_members(days=1, roles=sync_roles, reason=reason)
    print("Pruned:", sync_pruned)

sync.run(token, bot=False)