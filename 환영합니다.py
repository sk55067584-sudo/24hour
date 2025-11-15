import discord

# ⚠️ [필수] 환영 메시지를 보낼 채널의 ID로 변경하세요.
# (채널을 우클릭 후 'ID 복사하기'로 얻을 수 있습니다)
WELCOME_CHANNEL_ID = 1437034153467187200 # 여기에 채널 ID를 입력하세요!

# ⚠️ [필수] 봇의 토큰으로 변경하세요.
BOT_TOKEN = "MTQzODc5NjkzNDM3NzY0MDAyOQ.GcZPFf.5rLeV-h3wUObAmyncMRiZfr1aHErawjrEkX1Bs"


# 서버 멤버 이벤트를 수신하기 위해 Intents 설정
# intents.members = True 설정을 하려면 개발자 포털에서 SERVER MEMBERS INTENT를 켜야 합니다.
intents = discord.Intents.default()
intents.members = True
intents.message_content = True # 메시지 콘텐츠를 읽을 일이 없어도, 관례상 켜두는 경우가 많습니다.

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """봇이 Discord에 성공적으로 로그인했을 때 실행됩니다."""
    print(f'✅ 봇이 로그인했습니다: {client.user}')
    # 지정된 환영 채널이 존재하는지 확인
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        print(f'📢 환영 메시지 채널이 설정되었습니다: #{channel.name}')
    else:
        print(f'❌ 경고: 채널 ID ({WELCOME_CHANNEL_ID})를 찾을 수 없습니다. ID를 확인하세요.')

@client.event
async def on_member_join(member):
    """새로운 멤버가 서버에 들어올 때 실행됩니다."""
    # 1. 메시지를 보낼 채널을 가져옵니다.
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    
    # 2. 채널이 유효한지 확인합니다.
    if channel:
        # 3. 임베드(Embed)를 사용하여 멋진 환영 메시지를 만듭니다.
        embed = discord.Embed(
            title=f"🎉 {member.guild.name}에 오신 것을 환영합니다! 🎉",
            description=f"반갑습니다, **{member.mention}** 님!",
            color=discord.Color.green() # 색상을 변경할 수 있습니다 (예: blue, red)
        )
        
        # 멤버의 프로필 사진을 썸네일로 설정 (URL이 없는 경우 기본 이미지 사용)
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        
        embed.add_field(
            name="현재 멤버 수", 
            value=f"저희 서버는 이제 **{member.guild.member_count}** 명의 멤버와 함께합니다!", 
            inline=False
        )
        
        # 4. 채널에 메시지를 보냅니다.
        await channel.send(embed=embed)
        print(f'➡️ {member.name} 님에게 환영 메시지를 전송했습니다.')
    else:
        print(f'❌ {member.name} 님이 입장했지만, 유효한 채널 ID가 없어 메시지를 보내지 못했습니다.')

# 봇을 실행합니다.

client.run("MTQzODc5NjkzNDM3NzY0MDAyOQ.GcZPFf.5rLeV-h3wUObAmyncMRiZfr1aHErawjrEkX1Bs")
