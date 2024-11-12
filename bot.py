import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTMwNTg2OTU1MDExNzQ1NzkzMA.GgnXxC.0_YL8sy5RN6NVebrKQBHK27RYdS5uiC2H9Xq5M'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Troop training costs data
troop_costs = {
    "Infantry": {
        1: {"Food": 87, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 0.749},
        2: {"Food": 150, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 0.957},
        3: {"Food": 154, "Wood": 72, "Stone": 0, "Iron": 0, "Gold": 1.196},
        4: {"Food": 154, "Wood": 101, "Stone": 12, "Iron": 0, "Gold": 1.528},
        5: {"Food": 204, "Wood": 44, "Stone": 31, "Iron": 0, "Gold": 1.919},
        6: {"Food": 361, "Wood": 0, "Stone": 30, "Iron": 0, "Gold": 2.456},
        7: {"Food": 247, "Wood": 134, "Stone": 24, "Iron": 7, "Gold": 3.102},
        8: {"Food": 299, "Wood": 0, "Stone": 29, "Iron": 18, "Gold": 3.913},
        9: {"Food": 332, "Wood": 195, "Stone": 35, "Iron": 12, "Gold": 4.965},
        10: {"Food": 377, "Wood": 176, "Stone": 41, "Iron": 19, "Gold": 5.520},
    },
    "Ranged": {
        1: {"Food": 87, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 0.749},
        2: {"Food": 135, "Wood": 16, "Stone": 0, "Iron": 0, "Gold": 0.957},
        3: {"Food": 199, "Wood": 24, "Stone": 0, "Iron": 0, "Gold": 1.196},
        4: {"Food": 268, "Wood": 27, "Stone": 3, "Iron": 0, "Gold": 1.528},
        5: {"Food": 351, "Wood": 35, "Stone": 5, "Iron": 0, "Gold": 1.919},
        6: {"Food": 443, "Wood": 45, "Stone": 6, "Iron": 0, "Gold": 2.456},
        7: {"Food": 389, "Wood": 67, "Stone": 7, "Iron": 8, "Gold": 3.102},
        8: {"Food": 449, "Wood": 65, "Stone": 10, "Iron": 11, "Gold": 3.913},
        9: {"Food": 539, "Wood": 78, "Stone": 12, "Iron": 14, "Gold": 4.965},
        10: {"Food": 646, "Wood": 94, "Stone": 15, "Iron": 16, "Gold": 5.520},
    },
    "Cavalry": {
        1: {"Food": 87, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 0.749},
        2: {"Food": 150, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 0.957},
        3: {"Food": 221, "Wood": 0, "Stone": 0, "Iron": 0, "Gold": 1.196},
        4: {"Food": 227, "Wood": 17, "Stone": 3, "Iron": 0, "Gold": 1.528},
        5: {"Food": 326, "Wood": 67, "Stone": 4, "Iron": 0, "Gold": 1.919},
        6: {"Food": 464, "Wood": 28, "Stone": 5, "Iron": 0, "Gold": 2.456},
        7: {"Food": 432, "Wood": 101, "Stone": 6, "Iron": 4, "Gold": 3.102},
        8: {"Food": 449, "Wood": 122, "Stone": 22, "Iron": 5, "Gold": 3.913},
        9: {"Food": 584, "Wood": 49, "Stone": 35, "Iron": 8, "Gold": 4.965},
        10: {"Food": 539, "Wood": 59, "Stone": 41, "Iron": 19, "Gold": 5.520},
    },
    "Siege": {
        1: {"Food": 52, "Wood": 38, "Stone": 0, "Iron": 0, "Gold": 0.749},
        2: {"Food": 90, "Wood": 65, "Stone": 0, "Iron": 0, "Gold": 0.957},
        3: {"Food": 132, "Wood": 96, "Stone": 0, "Iron": 0, "Gold": 1.196},
        4: {"Food": 170, "Wood": 117, "Stone": 6, "Iron": 0, "Gold": 1.528},
        5: {"Food": 204, "Wood": 177, "Stone": 8, "Iron": 0, "Gold": 1.919},
        6: {"Food": 206, "Wood": 269, "Stone": 12, "Iron": 0, "Gold": 2.456},
        7: {"Food": 247, "Wood": 268, "Stone": 15, "Iron": 3, "Gold": 3.102},
        8: {"Food": 262, "Wood": 285, "Stone": 26, "Iron": 5, "Gold": 3.913},
        9: {"Food": 287, "Wood": 312, "Stone": 35, "Iron": 9, "Gold": 4.965},
        10: {"Food": 269, "Wood": 351, "Stone": 52, "Iron": 13, "Gold": 5.520},
    }
}

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}.')

# Command to get troop training cost by type, tier, quantity, and training speed
@bot.command(name='got-train')
async def got_train(ctx, troop_type: str, tier: int, quantity: int, training_speed: float = None):
    troop_type = troop_type.capitalize()  # Capitalize for consistency
    if troop_type in troop_costs and tier in troop_costs[troop_type]:
        costs = troop_costs[troop_type][tier]
        
        # Calculate total costs by multiplying each resource by quantity
        total_food = costs['Food'] * quantity
        total_wood = costs['Wood'] * quantity
        total_stone = costs['Stone'] * quantity
        total_iron = costs['Iron'] * quantity
        total_gold = costs['Gold'] * quantity

        # Adjust gold cost if training speed is provided
        if training_speed is not None:
            adjusted_training_speed = 1 + (training_speed / 100)  # Convert percentage to decimal
            total_gold = round(total_gold / adjusted_training_speed)

        # Build the response message with bold headers and formatted numbers
        response = (
            f"Training costs for {quantity:,} {troop_type} Tier {tier}:\n"
            f"**Food:** {total_food:,.0f}\n"
            f"**Wood:** {total_wood:,.0f}\n"
            f"**Stone:** {total_stone:,.0f}\n"
            f"**Iron:** {total_iron:,.0f}\n"
        )
        
        # Only include gold cost if training_speed is specified
        if training_speed is not None:
            response += f"**Gold:** {total_gold:,}"
        
        await ctx.send(response)
    else:
        await ctx.send(f"No data found for {troop_type} Tier {tier}.")

# Help command to display usage instructions
@bot.command(name='got-help')
async def got_help(ctx):
    help_message = """
    ```Training Costs Calculator
    Command: !got-train <Troop_Type> <Tier> <Quantity> <Training Speed>

    Example: !got-train infantry 8 100000 456.12
    This will return costs to train 100,000 Infantry Tier 8 @ Training Speed of +456.12%

    Troop Types:
     - Infantry
     - Ranged
     - Cavalry
     - Siege
    ```
    """
    await ctx.send(help_message)

# Run the bot
bot.run(TOKEN)