from urllib import urlretrieve, urlopen
from threading import Thread, activeCount
from time import sleep
from json import loads
from os import path
from sys import exit

class Extractor:
    Queue = []
    __Limit = 50

    __DistSM2 = 'sm2'
    __DistSMW = 'smw'
    __DistKS = 'ks'
    __DistHUG = 'hug'

    def do(self, command, action, other):
        if not path.isdir(self.__DistSM2) or not path.exists(self.__DistSM2):
            print 'The destination folder doesn\'t exists: ' + self.__DistSM2
            exit()

        self.parse(action, other, self.fetch('http://xat.com/web_gear/chat/pow2.php'))

    def fetch(self, url):
        fetched = urlopen(url)
        fetched = fetched.read()

        try:
                parsed = loads(fetched)

                return parsed
        except Exception, e:
                print e
                return []

    def parse(self, action, other, data):
        if action == 'pss' or action == 'images':
            if other == 'latest' or other == 'all':
                data = data[6][1]

                for key in data:
                    self.Queue.append(key)

            if other == 'all' or other == 'old':
                default_pss = "allpowers,topman,subhide,mod8,zoom,nofollow,invert,mirror,noaudies,reghide,nopc,tempmod,hat,red,green,blue,light,heart,shuffle,animate,square,nameglow,cycle,hexagon,clear,boot,octogram,show,superkick,invisible,pink,31" + ",guestself,sinbin,diamond,purple,ttth,hands,hairm,hairf,fade,gag,costumes,six,dood,angel,mute,radio,fruit,sport,num,hush,halloween,anime,status,thanksgiving,snowy,christmas,count,stick,dx,tempmem,valentine,63" + ",blueman,party,irish,flashrank,easter,nopm,banish,circus,gkaoani,military,gline,bump,gkaliens,scifi,supporter,tempown,gcontrol,tickle,sea,silly,blastpro,flag,blastban,independence,blastde,summer,bad,rapid,horror,mint,blastkick,everypower" + ",winter,adventure,feast,single,link,shocker,fairy,namecolor,gkbear,angry,gscol,ugly,love,barge,gkkitty,fantasy,announce,hero,rankpool,spin,animal,music,gkpanda,unwell,events,zap,sins,outfit,wildwest,work,banpool,127" + ",beach,candy,gback,zodiac,flower,space,snakeban,stoneage,spaceban,dance,kpeng,nerd,matchban,school,silentm,punch,away,peace,kchick,carve,spooky,kdog,bot,manga,mazeban,gold,snowman,reindeer,santa,sparta,dunce,159," + "newyear,can,codeban,magicfx,spy,kduck,heartfx,carnival,topspin,movie,monster,kat,typing,ksheep,pulsefx,blobby,reverse,fuzzy,spiralfx,nursing,gsound,kbee,vortexfx,jail,zip,drip,moustache,whirlfx,doodlerace,olympic,aliens,191," + "matchrace,burningheart,snakerace,kpig,poker,pony,clockfx,drop,spacewar,speech,vampyre,treefx,claus,quest,lang,quest2,glitterfx,xavi,kmouse,eighties," + "foe,zombie,makeup,kheart,kmonkey,nuclear,stylist,spring,vote,hands2,eggs,223,hearts,kfox,kcow,sketch,led,seaside,hair2f,statusglow" + "super,wedding,germ,cactus,slotban,fourth,switch,cuboid,phasefx,marriage,romance,sticky,kickall,fruities,darts,weather,kangel,kdemon,autumn,eggy,redirect,ani1,scary,255,zwhack,halloween2,piracy,froggy,blackfriday,winterland,noel,toys,badge,celebrate,hogmanay,cooking,farm,divorce,arachnid,sweetheart,random,ladybug,cupcake,bitefx,luck,tongues,springflix,snail,eventstats,easteregg,butterflies,springy,naughtystep,coffee,hamster,287,dreams,gamefx,worldcup,rocks,yellowcard,ballfx,winner,cutie,summerflix"

                for key in default_pss.split(','):
                    self.Queue.append(key)
        elif action == 'topsh':
            if other == 'latest' or other == 'all':
                data = data[4][1]

                for key in data:
                    self.Queue.append(key)

            if other == 'all' or other == 'old':
                default_topsh = "1066,noface,loser,rockon,palms,thumbsup,thumbsdown,flip,shh,bye,hug,clap,backoff,hehe,hmm,crazy,ono,shrug,hairm2,hairm3,emo,nrd,punk,hairf2,hairf3,hairf4,g1,goth,ninja,cb,police,nurse,jester,sphinx,dhat,crown,partyhat,facemask,sherlock,prop,grad,dunce2,straw,ribbon,halo,cloud,pray,apple,lemon,pear,orange,plum,banana,shirt,soccer,football,shirts,ball,bb,foam,weight,trophy,helmet,cupw,pknlaugh,tort,pkn,wh,frk,mmy,cdn,grim,tomb,bat,ghost,dig,die,hypno,dizzy,rage,headband,fan,comeon,grin,grump,tear,awe,doh,pouty,maniac,squint,ahhh,quiver,haira1,haira2,haira3,haira4,haira5,astro,haira6,haira7,haira8,haira9,haira10,pilgrimm,pilgrimf,indian,indian2,indian3,chef,dining,feast2,eatleg,snows,beard,bell,cane,ches,elf,give,pole,sack,sball,scarf,sdeer,sfeet,shiver,sledge,slist,smound,spull,stock,tree,wreath,xb1,xb4,skiss,bulb,sgift,beat,bheart,cupid,card,hug2,hug3,ilu,lhand,ring,rose,rose2,pce,cd,sleep,fs,shift1,pawn1,bff1,frnt1,hat1,hat2,glow1,snows1,wb1,dunce1,badge1,fwp1,naughty1,yellow1,balloon,bride,cake,phat,clink,pdance,pdance2,pdance3,groom,photo,popper,toast,clover2,drink,igirl,iman,pot,rainbow,shi,tap,drum,bagpipes,basket,bunny,bunny2,chick,egg2,eggb,paintegg,kbiggrin,kclap,kconfused,kcool,kcrying,kdizzy,keek,keyerub,kfit,kfrown,kglare,khehe,khello,khug,kkiss,klove,kmad,kmischief,knod,krant,kredface,ksad,ksleepy,ksmile,ksmirk,kstraight,kstruggle,ktongue,kun,kwink,acrobat,balloonart,cannon,clown,eleride,fireblow,firewand,highwire,uniwire,juggler,lion,splat,tamer,uni,unirope,wheel,camo,coastguard,drillserg,gasmask,m1h,marine,pilot,sailor,sailor2,salute,smoke,kachat,kacrazy,kafang,kafill,kagab,kagrin,kagsp,kalook,kao,kaoo,kapunch,kaswt,katalk,katear,katears,kaum,kaupset,kawink,alien2,alienb,beam,blob,borg,cylon,jetpack,laser,vial,vr,ufo,cheerleader,horn,pennant,corndog,vuvu,fish,fish2,fish3,bubbles,crab,diver,dolphin,jellyfish,octopus,shrimp,starfish,turtle,weed,bonk,burp,crazy2,dopey,impact,irked,itchy,mischief2,nose,raspberry,rolleye,spit,string,abe,bbq,flagwave,fwlaunch,glowstick,liberty,sparkler,starbounce,starburst,starring,tiphat,usface,usss,beachbbq,cooler,efan,fishing,frisbee,goggles,kayak,laytowl,pina,sanddig,sandplay,bands,towl,waterbottle,waterskii,biker,slingshot,thief,fbomb,liar,mist,franken,goblin,knife,pkncut,spider,triclops,vamp,warewolf,hit,dodge,lob,mobounce,moring,campfire,canopy,compass,firstaid,hangglider,hunting,lantern,map,marshmallow,iceaxe,swing,waterskiing,zipline,smokes,asif,one,heartburst,heartbounce,noway,duck,electrocute,eyepop,flamed,lookaround,scream,wow,dazed,hazey,drool,footmouth,mindblow,misspeak,relieved,uvula,arc,butterfly,fcrown,fhair,fhat,flower2,frog,fwings,heartwand,mushrooms,shards,kbawe,kbcold,kbcry,kbdance,kbpunch,kbsad,kbscream,kbweep,kbwink,kbyawn,explode,facepalm,bite,hissyfit,mutter,potstir,pullhair,raging,ticked,yell,flame,grumpy2,headache,timebomb,uangel,udemon,uevil,uhappy,ulook,uthink,usad,uscratch,usmile,utongue,uwink,carolers,decortree,giftdrop,giftrattle,gingerbread,pullsled,antler,shovel,accident,snowboard,snowfight,snowm,xface,snowmobile,ornament,earmuffs,snowglobe,cold,freezing,snowover,snowangel,windy,icecube,bowleat,burger,burgerlook,candycorn,carrot,cherry,chicken,chili,chipeat,coffeesplash,donut,eatspagetti,eattakeout,eggcook,eggplant,fortunecookie,fries,icecream,icecreameat,peanut,popcorn,pretzel,soupeat,spam,stirpan,takeout,thinkfood,toast2,pizza,kkbiggrin,kkconfused,kkcool,kkcrying,kkd,kkdance,kkdead,kkeek,kkfrown,kkhide,kkhug,kkmad,kknme,kkpaws1,kkpaws2,kkpaws3,kkredface,kkscn,kkshock,kksleepy,kksmile,kkstraightface,kkstruggle,kktongue,kkun,kkwary,kkwink,kkx3,kkxd,kkyawn,axe,darkeyes,dragon,flail,hole,helmet2,medusa,orcm,elf2,ogre,orcf,invis,scroll,slash,smskull,sword,wizard,daggers,electro,epi,fireball,flying,genie,iceman,invisi,jekyl,maddr,telekin,amazon,upaway,ripshirt,doggy,giraffe,goat,lion2,monkey,mouse,panda2,raccoon,sheep,unicorn,disco,dj,drums,flute,guitar,harp,piano,trumpet,violin,zippo,kpfit,kpembarassed,kppaws,kpd,kpannoyed,kppaws2,kplove,kpjoy,kpcrying,kphurt,blownose,chill,cough,icepack,sickface,sneeze,soup,thermometer,crutches,feint,cough2,headknock,sweats,coy,flirt,freehugs,heartbeat,heartblow,ihu,lovedraw,ucute,uhot,cringe,shake,shocking,envy,gluttony,greed,lust,pride,sloth,wrath,whip,turban,tophat,tinfoil,sombrero,paperbag,paperbag2,grandpa,grandma,glassesslip,disguise,curlers,braces,blindfold,beret,undertaker,sheriff,ropeg,ropeb,push,prospector,outlaw,native,bullride,bartender,officeworker,driver,doctor,chef2,burgerflipper,blacksmith,astronaut,teacher,stewardess,shepherd,scientist,plumber,paperboy,miner,mechanic,judge,journalist,gardener,fortuneteller,fireman,icman,lifeguard,lotion,metaldetect,sandbury,sandfun,shkhat,sunburn,surf,tanning,candy,cdycorn,cdyback,donuteat,eatchoco,floss,gum,lolipop,mm,aries,taurus,gemini,cancer,leo,virgo,libra,scorpio,sagittarius,capricorn,aquarius,pisces,fangry,fcry,fcool,feek,fconfused,ftongue,fredface,fsleepy,fbiggrin,fsad,fwink,eclipse,meteorite,nasa,radiotele,rocket,satellite,saucer,shuttle,space,telescope,sncool,sneek,snredface,snconfused,snfrown,snbiggrin,snangry,snsleepy,sncry,snsmile,snwink,caveman,dino,cavewoman,cavework,cavebeard,caveclothes,torch,spear,rocksmash,cavehair,boneswing,wallart,stickfire,cavebeard2,moonb,dance1,dance2,dance3,dance4,dance5,dance6,dance7,dance8,dance9,dance10,dance11,kpesneeze,kpeshy,kpeshame,kpejoy,kpeglare,kpefit,kpedots,kpedizzy,kpeclap,kpeangry,kpedance,kpepop,aplus,bowtie,brain,coder,gates,nglasses,nsci,phone,read,calc,backpack,daycare,gts,punished,rubber,schoolgirl,sbell,studying,tabsc,teacher2,writing,pconfused,pcrying,pcute,pdead,pfury,pgiggle,pglare,pjump,pmanic,punched,pshades,pshy,psleepy,pthink,dove,dove2,dove3,hglass,phair1,phair2,phair3,rbe,reggae,kccrying,kcdizzy,kceek,kcglare,kclook,kcsad,kcsmug,kctongue,kcwink,carveduh,carvegrin,carvescream,carvesly,carvesmile,dracula,grim2,pknhide,vampire,sixeyes,bat2,blackcat,blackwidow,ghost2,hockeymask,plant,bloodyknife,scarecrow,kdcheer,kdcrazy,kddead,kdfit,kdglare,kdsad,kdshocked,kdsleepy,kdsmile,kdtired,kdwoo,bot2,bot3,bot4,bot5,manga1,manga2,manga3,manga4,manga5,manga6,manga7,manga8,manga9,manga10,manga11,manga12,manga13,manga14,manga15,manga16,manga17,goldb,bars,bar,goldstar,smcry,smgrin,smlaugh,smredface,smsad,smshocked,smsleepy,smtongue,smmad,smcool,resurprised,resmirk,resleepy,resad,reredface,relaugh,reglare,recry,recool,reangry,renose,reback,sabiggrin,saconfused,sacry,saglare,saredface,sasad,sastraightface,sasurprised,satongue,sawink,spartayell,getready,helmet3,soldier,spants,spartafight,spartan,spartan2,truewar,xerxes,duh,doh2,calendar,celebration,champagne2,champagneback,clink2,firework1,firework2,nyball,nyhat,nykiss,nyparty,sparkler2,canangel,canbounce,cancontempt,canfury,canoo,canshifty,canthink,cantwitch,canum,canun,crosshair,folder,footprints,headset,keyhole,keypad,peeking,radar,spydrink,spyeye,spying,spypaper,spyrope,kduckback,kduck1,kduck2,kduck3,kduck4,kduck5,kduck6,kduck7,kduck8,kduck9,kduck10,kduck11,kduck12,heartfx,heartfx2,heartfx3,anonmask,beads,brazilboom,carniphant,cjester,cmask,flowersquirt,headdress,kreu,shakeit,wannasamba,yeayea,cjester2,cbird,cangel,action,admission,booth,cameraman,director,drink2,film,filmroll,pose,tickets,mangel,mbat,mbear,mchick,mdrip,mfish,mglare,kat1,kat2,kat3,kat4,kat5,kat6,kat7,kat8,kat9,kat10,katback,typing1,ksheep1,ksheep2,ksheep3,ksheep4,ksheep5,ksheep6,ksheep7,ksheep8,ksheep9,ksheep10,ksheepback,pulsefxback,bbclap,bbconfused,bbcry,bbfit,bbglare,bbhug,bblaugh,bboops,bbpout,bbwink,bbback,fzangel,fzback,fzbiggrin,fzcool,fzcrazy,fzd,fzdance,fzsad,fzstretch,fztongue,fztwirl,spiralfx2,crazyn,nblood,nbroken,ndoc,nlist,nmask,nne,noxy,nsurg,megap,volume,tooloud,canthear,playbtn,kbeeback,kbeeclap,kbeecry,kbeed,kbeedance,kbeefedup,kbeejoy,kbeemad,kbeepunch,kbeexx,kbeeyay,vortexfx2,ballchain,bobby,copstop,cracker,cuffs,gavel,handsair,jailnumber,mugshot,prisoner,dripclap,dripdance,dripeek,dripfit,dripglare,driphehe,driphello,driphug,driplaugh,dripsad,dripshocked,driptired,dripxd,dripyell,moustache1,moustache2,moustache3,moustache4,moustache5,moustache6,moustache7,moustache8,moustache9,bronzem,goldm,oboxing,ocycling,odiving,ogymnastics,ohurdles,orowing,orunning,oswimming,otennis,otorch,ovolleyball,silverm,oarchery,obasketball,ofencing,ohockey,aliens,alilaugh,alidead,aliclap,alid,alilove,aliscratch,alitalk,alicry,alitongue,aliyay,aliback,bheartb,kpigangry,kpigback,kpigball,kpigfraz,kpiglove,kpigmad,kpigmud,kpigpals,kpigsleep,kpigsnoot,kpigwrite,pclubs,pobluff,pochips,pod,pogirl,poplayer,povip,powin,poyay,pspades,pdiamonds,phearts,poback,pocall,poclap,pocry,poeat,pofan,poglasses,pohay,pomane,ponyd,powhip,clockfx2,clockfx3,clockfx4,dropworry,dropumb,dropscratch,droprub,drophey,dropeat,dropdance,dropclap,dropback,spd,spfrus,spyay,spkiss,splap,splove,spvamp,spwrite,spxmas,sppup,spback,gifts,vbat,vbheart,vblood,vcoffin,vcross,vfangs,vglamour,vrip,vstake,vtongue,clcool,cld,cleek,clgrin,clmad,clsad,clsmile,clsweat,clwink,clx,bearer,disappear,dwarf,goblin2,queenelf,sneak,thering,warrior,wizzard,agreement,arrow,burnt,dwarf2,dwarfz,elve2,goblin3,newton,pile,kmcheer,kmcry,kmeyerub,kmfit,kmfrustrate,kmglare,kmgrouch,kmhide,kmhug,kmlaugh,kmshock,kmshuffle,kmsleepy,kmsmile,kmback,bighair,bigphone,boombox,cassette,dance80,dj80,hoverboard,joystick,skate,slacker1,slacker2,poi,thermochrome,timemachine,zombie1,zombie2,zombie3,zombie4,survivor1,survivor2,survivor3,survivor4,bloodface,deadup,zombieback,blush,comb,eyeliner,lipgloss,lipstick1,lipstick2,makeupface,nailpolish,perfume,purse,kharrow,khbub,khcupid,kheartb,kheyes,khhug,khhurt,khily,khkiss,khlips,khmadly,khring,khroses,kmoback,kmoblow,kmod,kmodance,kmofrus,kmonehneh,kmorage,kmoredface,kmostare,kmoteeth,kmoun,kmowhistle,kmowonder,nuclearb,barber,mirror2,shave,shair1,shair2,shair3,shair4,shair5,shair6,shair7,bees,birdy,butterflys,flohat,flohide,flowerbed,flowers,floshow,inflower,rainbow2,springhat,watercan,watercan2,bemused,cross,tick,placard,voting,voting2,hands2,pointing,prosper,peace2,notlistening,heehee,hearno,daydreaming,cutthroat,callme,crossed,highfive,chickwalk,eggnod,eggbroke,stripegg,eggwink,eggsleep,bunnyears,eggtongue,basket2,kfoxbino,kfoxcry,kfoxd,kfoxggl,kfoxinl,kfoxpsy,kfoxshades,kfoxsleep,kfoxtant,kfoxtwag,kfoxwhat,kwangry,kwbell,kwcry,kwd,kwfrus,kwlaugh,kwlove,kwmad,kwnod,kwscratch,kwsleepy,kwswt,kwwhat,kwyay,skannoyed,skd,skdead,skfrus,skgrr,skoo,sksad,sksix,sksmile,skwink,skback,beachdrink,beachvolley,coconut,crab2,dolphin2,flipflops,sandcastle,seatree,shell,hair2f1,hair2f2,hair2f3,hair2f4,hair2f5,hair2f6,hair2f7,hair2f8,hair2f9,hair2f10,sumad,susmile,sulove,susad,sulaugh,sucool,sutongue,sudead,suconfused,suredface,sucry,suback,roses,cakecut,arch,dovew,flowersw,givering,invitation,throwboquet,weddingcake,germ2,germ3,germ4,germ5,germ6,germ7,germ8,germ9,germ10,cactongue,caccool,cacwhat,cacdead,cacflaming,cacpanic,cacblow,cacmad,cacsmile,caclove,cacback,slotbar,cherries,orange2,plum2,seven,spinbutton,flagfw,fourthcal,fwbang,iwantyou,showcal,usafw,usafws,watchfw,waveflagf,waveflagm,cubiggrin,cucat,cucool,cucry,cumaracas,cusad,cushine,cusmile,custar,cuback,phaseheart,phaseplan,phaseques,cake2,catchboquet,groom2,bride2,propose,showring,twohearts,weddingdrink,weddingring,affection,cuddle,formal,hearthands,huba,hugme,iheart,kisses,lashes,serenade,stangel,stattention,stcool,stcrying,stdevil,stheart,stlips,stsleepy,stwhat,frapple,frbanana,frgrapes,frkiwi,frlemon,frmelon,frorange,frpear,frpineapple,frstrawberry,dart,dartthrow,cleary,coldthermo,foggy,hotthermo,rainy,snowy2,stormy,sunny,sunshine,tornado,windy2,kancloud,kancry,kandizzy,kangoo,kanjoy,kanlove,kanroses,kanthink,kantired,kdefear,kdefire,kdejoy,kderage,kderain,kdestir,kdesweat,kdetri,kdewar,acorn,gotleaf,jam,leaf,leaves,mushrooms2,scarecrow2,squirrel,sunflower,eggzzz,eggupset,eggtickoff,eggthumbs,eggshh,eggyes,egggamer,eggcross,eggcool,eggback,redirect2,a1adore,a1cry,a1evil,a1eww,a1fan,a1fedup,a1fx,a1heh,a1hot,a1love,a1pff,cobweb,coffin,pknburning,scarybat,scaryeyes,scaryghost,scaryhat,scarytree,tomb2,mallet,bloodgirl,docmask,madhat,madsci,scissor,whitehair,zbride,zdoc,zgirl,barrel,handhook,octopus2,piratebird,piratemap,pirateship,telescope2,toxicdrink,trove,frcool,frmad,frooo,frcry,frbiggrin,frdead,frsad,frchkl,frlove,bagfight,bags,bargain,cart,cashhere,cashreg,lowprice,manybags,pricetag,ornament2,chimney,fishing2,glove,snowman2,winterhouse,iceheart,wlamp,wtree,angelf,angelm,snowmanf,snowmanm,mrsanta,mrssanta,reindeerm,gingerman,gingerwoman,reindeerf,bearftoy,bearmtoy,cartoy,dolltoy,ducktoy,helicoptertoy,locomotivetoy,puzzletoy,pyramidtoy,spinningtop,celbday,celbottle,celcnny,celdance,celdrunk,celflag,celgrad,celhorn,celvictory,celyeah,countdown,firecracker,firecracker2,nyballoons,nyclock,nyfireworks,nysparkler,year,blender,chop,cookkiss,flipburger,flipegg,knead,serving,stir,whisk,cornback,cowface,eggs2,growing,milking,rooster,scarecrw,sheepback,sugarcane,tomatoes,wmback,divsplit,divring,divnolove,divm,divf,divbreak,botf,botm,brokenheart2,dhammer,sadflower,ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,candleheart,cupidheart,fourteenth,keylove,letterlove,swans,sweetheart,treelove,varrow,vballoons,lbfly,lbshock,lbcry,lbdizzy,lbahh,lbmad,lbkiss,lblove,lbd,lbdead,lbbehind,cchappy,ccsad,ccbeye,ccscn,ccsleepy,ccredface,ccangry,ccnono,cccry,ccback,broccoli,jelly,sweet,sheep2,pwalking,potofgold,horseshoe,harp2,goldclover,clovers,beer2,pballoons,luckbh,tobig,tocheeky,toeeh,tohaught,toneener,topfft,tostarry,toteeth,tothirsty,tocircle,butterfly2,springflower,springleaf,sunflower2,rflowers,snail1,snail2,snail3,snail4,snail5,snail6,snail7,snail8,snail9,snail10,snailb,birdyeggs,carrots,chicken2,easterbasket,ebutterfly,eggchoco,inegg,rabbit,sleepyegg,bfb,butterflies2,butterflies3,butterflies4,butterflies5,butterflies6,butterflies7,butterflies8,butterflies9,butterflies10,sprevil,sprtired,sprcrazy,sprangry,sprexhausted,sprthumbs,sprfrus,sprjump,sprtongue,sprback,cappuccino,coffeebeans,coffeemachine,coffeesack,fhand,kettle,lovecoffee,mhand,sugar,habounce,harock,hasway,hacry,hasleep,hajump,hajoy,haangry,haexcite,hadream,hamsterback,climbing,dreaming,dreamsbh,glowworm,indream,lovedream,night,scarydream,zsleep,grow,starman,screwattack,bubble,ghosteat,coinfx,fball,changes,corner,goal,goldball,player,training,vuvu2,whistle,breakfx,rollingfx,roteeth,rolook,rostar,rocute,rofrown,roahah,rodizzy,roblinky,rolove,rosmirk,basketball,bowling,jugglerball,rollingball,laurel,podium,ribbon2,ticker,trophy2,winnerflag,winning,wtape,cuangry,cubear,cubow,cubunnyears,cuchilled,cuexcited,cuhappy,cupleased,curage,cutired,cuunhappy,scrab,sfan,shell2,sunny2"

                for key in default_topsh.split(','):
                    self.Queue.append(key)
        elif action == 'hug':
            if other == 'latest' or other == 'all' or other == 'old':
                data = data[3][1]

                for key in data:
                    self.Queue.append(key)
        elif action == 'backs':
            if other == 'latest' or other == 'all':
                data = data[1][1]

                for key in data:
                    self.Queue.append(data[key])

            if other == 'all' or other == 'old':
                default_backs = "heart,square,hexagon,clear,octogram,diamond,apple,lemon,pear,fruit,orange,plum,banana,shirt,soccer,football,pkn,tomb,snowy,tree,stock,bulb,balloon,eggb,camo,blob,alienb,gkaoani,gkaliens,independence,usface,fish,crab,octopus,jellyfish,starfish,shrimp,sea,electrocute,flame,timebomb,ornament,ogre,frog,flower2,gkbear,gkkitty,gkpanda,sheriff,cdycorn,cdyback,zodiac,flower,snakeban,moonb,brain,kpeng,sbell,tabsc,peace,punch,noface,carve,bot4,kdog,goldb,mazeban,goldstar,snowman,santa,reindeer,reback,champagneback,can,kduckback,heartfx,heartfx2,heartfx3,monster,katback,ksheepback,pulsefxback,bbback,fzback,kbeeback,drip,doodlerace,aliback,kpigback,poback,dropback,spback,kmback,tv80,zombieback,kheartb,kmoback,eggsleep,kfox,kcow,skback,suback,germ,germ2,germ3,germ4,germ5,germ6,germ7,germ8,germ9,germ10,cacback,cuback,fruties,frapple,frbanana,frgrapes,frkiwi,frlemon,frmelon,frorange,frpear,frpineapple,frstrawberry,eggback,badge,cornback,sheepback,wmback,ccback,springleaf,sunflower2,snailb,eventstats,bfb,sprback,hamsterback"

                for key in default_backs.split(','):
                    self.Queue.append(key)
        elif action == 'smileys':
            default_smileys = "redface,rolleyes,hi,meh,ugh,a,sry,crs,un,d,scn,nod,gagged,nme,swt,roll,rofl,chkl,inlove,blk,xp,eyes,tired,smirk,ill,dead,hello,yum,think,mischief,zip2,puke,yawn,swear,cry2,what,omg,o_o,goo,smirk2,beye,wary,shock,xd,cyc,wt,chew,contempt,fedup,aghast,look,spin2,tipsy,twitch,shifty,ashamed,pty,sad,rolling,no,jolly,annoyed,astonished,evil,sinister,sour,um,dream,memory,babythrow,candyeat,cute,flowerthrow,gloomy,hey,hula,loving,meloneat,shadesoff,stressing,waiting,ugc,hearts2"
            default_smileys += "peach,xana,x,chest,gst,alien,bby,bot1,tox,8ball,eye,kirb,pm,pmg,inv,inv2,inv3,sonic,shadow,mario,luigi,mushroom,yoshi,countb,ness,smashball,mephiles,tri,lucario,nights,arbiter,link,mewtwo,xj9,hk,lolwut,kermit,beaker,beast,dv,homer,3tomoe,mangekyou,pikachu,pball,wwe,sm,a1,nko,x3,dog,cat,pig,mk,penguin,panda,bear,cc,ccc,cotton,pie,c,b,o,i,t,mo,so,sb,oo,p,ph,yt,dmd,bin,ush,ipod,ip,sun,rain,r,f,li,l,u,y,n,grl,boy,scb,bio,rad,pgm,mgp,ao,star,note,hex,yy,moon,rubik,cir,cdy,deer,snta,g,sman,xday,xtre,xstk,mtoe,hly,egg,ghat,clover,stickman,stickman2,stickman3,stickairguitar,stickkungfu,stickangry,stickymca,danny,turkey,ss,qbone,mc,lb,mario8,nop,okp,mate,amy,mouser"

            for key in default_smileys.split(','):
                self.Queue.append(key)
        elif action == 'kisses':
            default_kisses = "Confetti,Hearts,Champagne,Argue,Cry,Hippo,Hearts,Paint,Surprise,Magic8ball,Airplane,Parachute,Dynamite,Lips,Bomb,Fireworks,Pull,Shark,Blood,Globe,Bugs,Grumpy,Snow,Ttth"
            default_kisses += "Marriage,Marry,Rings,Sunset,Hippod,Divorce,Divorced,Botd"

            for key in default_kisses.split(','):
                self.Queue.append(key)

        if action == 'images':
            self.download('/images/smw/')
        elif action == 'kisses':
            self.download('/images/ks/')
        elif action == 'hug':
            self.download('/images/hug/')
        else:
            self.download()

    def download(self, url="/images/sm2/"):
        queueLen = len(self.Queue)

        try:
            i = 0
            while i < queueLen:
                while activeCount() < self.__Limit and i < queueLen:
                    print 'Downloading: ', self.Queue[i], '{0}/{1}'.format(i + 1, queueLen)
                    Thread(target = self.retrieve, args = [self.Queue[i], url]).start()
                    i += 1
                sleep(1)

            print 'Please wait, finishing pending tasks...'
        except Exception, ex:
            print ex

    def retrieve(self, name, url):
        ext = ".swf"
        dist = self.__DistSM2

        if url == "/images/smw/":
            dist = self.__DistSMW
            ext = ".png"
        elif url == "/images/ks/":
            dist = self.__DistKS
        elif url == "/images/hug/":
            dist = self.__DistHUG
                
        while True:
            try:
                urlretrieve("http://xat.com" + url + name + ext, dist + "/" + name + ext)
                break
            except Exception, e:
                print e
                pass
