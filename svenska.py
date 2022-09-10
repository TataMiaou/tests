from redbot.core import commands
from random import *

class svenska(commands.Cog):
    """Vadå?"""
    @commands.command()
    async def svenska(self, ctx):
        """Jävla skit!"""
        sv = [
            "**VAD FAN ?**",
            "**HERREGUD**",
            "SAAB är mycket bättre",
            "**Gå åt helvete!**",
            "Pissdåligt, som vanligt.",
            "Nämen lilla vännen...",
            "Vem **FAN** tror du att du är?",
            "PK.",
            
        ]
        phrase = sv[randint(0, len(jmb) - 1)]
        await ctx.send(phrase)
