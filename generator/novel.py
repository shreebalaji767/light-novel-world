import hashlib, secrets, random

GENRES = [
 ('Dark Fantasy','gothic',['ominous','melancholic','mysterious']),
 ('High Fantasy','storybook',['grand','mythic','hopeful']),
 ('Isekai','portal',['wonderous','energetic','adventurous']),
 ('Romance','editorial',['tender','wistful','intimate']),
 ('Romantic Fantasy','velvet',['dreamlike','tender','dramatic']),
 ('Mystery','archive',['curious','tense','secretive']),
 ('Psychological Thriller','clinical',['uncertain','tense','introspective']),
 ('Horror','warning',['dreadful','quiet','uncanny']),
 ('Science Fiction','mission',['vast','curious','philosophical']),
 ('Cyberpunk','terminal',['neon','restless','urgent']),
 ('Post-Apocalyptic','journal',['bleak','resilient','hopeful']),
 ('Wuxia','ink',['poetic','disciplined','reflective']),
 ('Xianxia','celestial',['mythic','transcendent','mysterious']),
 ('Slice of Life','notebook',['warm','gentle','nostalgic']),
 ('Comedy','comic',['playful','chaotic','absurd']),
 ('Historical Fantasy','manuscript',['ornate','political','dramatic']),
 ('Mecha','blueprint',['technical','heroic','urgent']),
 ('Time Travel','clockwork',['strange','urgent','melancholic']),
 ('Supernatural','moonlit',['mysterious','quiet','uncanny']),
 ('Steampunk','industrial',['inventive','adventurous','ornate'])]

NAMES=['Aren Vale','Mira Solenne','Kael Rowan','Elian Voss','Neris Ash','Liora Fen','Tarin Wren','Sera Noct','Iven Marr','Rhea Calder','Noah Vey','Cassian Roe','Vera Quill','Ren Aster','Mika Dorne','Ari Bell','Kieran Holt','Nyla Soren','Eris Vale','Jun Arclight']
PLACES=['Veyra','Aster','Namar','Orison','Lowglass','Cael','Bellmere','Meridian','Elowen','Sahr','Saint Rook','Hollow March','Ilyon','Brasshaven','Selene']
FACTIONS=['Lantern Court','Ninth Archive','Silver Assembly','Ashen Guild','Meridian Order','Hollow Choir','Crownless Council','Night Cartographers','Glass Syndicate','Azure Sect','Red Observatory','Clockwork Union']
POWERS=['memory-weaving','shadow cartography','resonance magic','name-binding','dream architecture','gravity singing','echo manipulation','ink sorcery','star navigation','time-threading','spirit bargaining','machine empathy','weather shaping','oath magic','mirror walking']
OBJECTS=['a cracked silver key','a book with no title','a mechanical bird','a black compass','a sealed glass seed','a sword that reflects memories','a red umbrella','a clock that counts backward','a map that changes at night','a coin bearing an unknown king','a broken ceremonial mask']
CONFLICTS=['someone is quietly erasing the city’s history','a forbidden signal is arriving from a place that should not exist','an ancient agreement is beginning to fail','people are dreaming the same impossible dream','the ruling institution has hidden the disappearance of an entire district','a dead person’s letters are arriving years after their death','a sealed power has begun choosing ordinary people','the protagonist discovers that their most important memory is false','a border closed for a century has suddenly opened','a festival repeats the same day every year']
ADJ=['Silent','Last','Hidden','Fallen','Forgotten','Crimson','Hollow','Midnight','Silver','Glass','Ashen','Infinite','Broken','Wandering','Borrowed','Vanishing','Sleeping','Nameless','Electric','Moonlit']
NOUN=['Crown','Bell','Archive','Kingdom','Letter','City','Signal','Garden','Sword','Memory','Station','Moon','Clock','Throne','Library','Road','Tower','Sea','Door','Name']
BEATS=['an unexpected discovery changes the protagonist’s ordinary routine','a stranger delivers a warning that makes no immediate sense','the protagonist follows a clue into a forbidden place','an apparent ally reveals a hidden connection','the protagonist learns the conflict is larger than expected','a small victory creates a dangerous consequence','the protagonist chooses between protecting someone and learning the truth','a forgotten detail from the past becomes important','the antagonist makes its first unmistakable move','a revelation changes the meaning of an earlier event']


def fp(parts): return hashlib.sha256('||'.join(str(x).lower().strip() for x in parts).encode()).hexdigest()

def title(r):
    choices=[f'The {r.choice(ADJ)} {r.choice(NOUN)}',f'{r.choice(NOUN)} of the {r.choice(ADJ)} {r.choice(NOUN)}',f'The {r.choice(NOUN)} That {r.choice(["Returned","Forgot","Remembered","Awakened","Vanished"])}',f'When the {r.choice(NOUN)} Returned',f'{r.choice(ADJ)} {r.choice(NOUN)}']
    return r.choice(choices)

def make_character(r,role):
    return {'name':r.choice(NAMES),'role':role,'traits':r.sample(['patient','reckless','observant','sarcastic','reserved','idealistic','pragmatic','curious','stubborn','gentle','ambitious','secretive'],3)}

def generate_novel():
    r=random.Random(secrets.randbits(256))
    genre,visual,moods=r.choice(GENRES)
    protagonist=make_character(r,'protagonist'); ally=make_character(r,'ally'); rival=make_character(r,'rival')
    place=r.choice(PLACES); faction=r.choice(FACTIONS); power=r.choice(POWERS); obj=r.choice(OBJECTS); conflict=r.choice(CONFLICTS)
    t=title(r)
    chapter_count=r.randint(8,12)
    chapters=[]
    used=set()
    for i in range(1,chapter_count+1):
        beat=r.choice([b for b in BEATS if b not in used] or BEATS); used.add(beat)
        ct=r.choice([f'The {r.choice(ADJ)} Clue',f'The {r.choice(NOUN)} Returns',f'Someone Was Waiting',f'The Rule That Was Missing',f'An Answer With Teeth',f'Before the Truth'])
        paras=[
          f'The morning began quietly in {place}, which was exactly why {protagonist["name"]} noticed the change.',
          f'This chapter turns on one development: {beat}.',
          f'{ally["name"]} arrived with questions, while {rival["name"]} offered an answer that sounded reasonable until its final sentence.',
          f'The strange rules of {power} became clearer only after {protagonist["name"]} examined {obj}.',
          f'The problem was larger than the central mystery. Every answer created another question, and every familiar detail became less trustworthy.',
          f'By evening, {protagonist["name"]} had made a decision. There would be no returning to the old routine.',
          f'Far away, something connected to the {faction} answered.',
          f'Chapter {i} ended without resolving the mystery. It only made the next question impossible to ignore.'
        ]
        chapters.append({'number':i,'title':f'Chapter {i:02d} — {ct}','paragraphs':paras})
    palettes=[('#0c1016','#171e28','#65c4d5','#e8f1eb'),('#151218','#28202e','#c36a8d','#f0dfd2'),('#11130f','#242a20','#a89455','#e8e0ca'),('#111111','#202020','#d28c48','#eee5d4'),('#0b1020','#172743','#718cff','#e5edff')]
    colors=r.choice(palettes)
    layouts=['centered','split','editorial','immersive','dashboard','asymmetric','book','terminal']
    design={'mode':visual,'layout':r.choice(layouts),'radius':r.choice(['0px','8px','14px','22px','30px']),'serif':r.choice([True,False]),'bg':colors[0],'surface':colors[1],'accent':colors[2],'text':colors[3]}
    story_fp=fp([t,genre,place,faction,power,obj,conflict,[c['name'] for c in [protagonist,ally,rival]],design['mode'],design['layout']])
    return {'id':story_fp[:16],'genre':genre,'visual':visual,'mood':r.choice(moods),'title':t,'subtitle':f'{genre} · {visual.title()} edition','synopsis':f'In {place}, {protagonist["name"]} discovers {obj}. At the same time, {conflict}. To survive, they must confront the {faction} and learn to use {power} before the hidden truth reaches everyone.','location':place,'faction':faction,'power':power,'object':obj,'conflict':conflict,'protagonist':protagonist,'characters':[ally,rival],'chapters':chapters,'design':design}
