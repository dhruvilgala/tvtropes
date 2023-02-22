# Analyzing Gender Bias in Narrative Tropes

## Abstract

Popular media reflects and reinforces societal biases through the use of tropes, which are narrative elements, such as archetypal characters and plot arcs, that occur frequently across media. In this paper, we specifically investigate gender bias within a large collection of tropes. To enable our study, we crawl [tvtropes.org](http://tvtropes.org), an online user-created repository that contains 30K tropes associated with 1.9M examples of their occurrences across film, television, and literature. We automatically score the “genderedness” of each trope in our TVTROPES dataset, which enables an analysis of (1) highly-gendered topics within tropes, (2) the relationship between gender bias and popular reception, and (3) how the gender of a work’s creator correlates with the types of tropes that they use.

## Paper
Here is the [official page for our paper.](https://www.aclweb.org/anthology/2020.nlpcss-1.23/)

## Data
We crawled TVTropes.org to collect a large-scale dataset of 30K tropes and 1.9M examples of their occurrences across 40K works of film, television, and literature. We then connected our data to meta-data from IMDb and Goodreads to augment our dataset and enable analysis of gender bias.

Our data can be found [here (~650 MB)](https://drive.google.com/file/d/1Duyz5ATlLHzwMidj15bWVnWHpdE4aRXn/view?usp=sharing). It contains the following:
- tropes contains trope names, IDs, and descriptions
- lit_tropes, film_tropes, and tv_tropes contain the trope names, titles, and examples across each form of media
- lit_goodreads_match, film_imdb_match, tv_imdb_match contain the tropes, examples, and titles linked to the metadata

Samples of each table are shown at the end of this document.

## Code
Each script contains the code for each different analysis conducted in the paper. Please ensure you have the requirements listed in requirements.txt installed to run the scripts. 

## Citation

If you use this dataset or code for your research, please cite:

```
@inproceedings{gala-etal-2020-analyzing,
    title = "Analyzing Gender Bias within Narrative Tropes",
    author = "Gala, Dhruvil  and
      Khursheed, Mohammad Omar  and
      Lerner, Hannah  and
      O{'}Connor, Brendan  and
      Iyyer, Mohit",
    booktitle = "Proceedings of the Fourth Workshop on Natural Language Processing and Computational Social Science",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.nlpcss-1.23",
    doi = "10.18653/v1/2020.nlpcss-1.23",
    pages = "212--217",
    abstract = "Popular media reflects and reinforces societal biases through the use of tropes, which are narrative elements, such as archetypal characters and plot arcs, that occur frequently across media. In this paper, we specifically investigate gender bias within a large collection of tropes. To enable our study, we crawl tvtropes.org, an online user-created repository that contains 30K tropes associated with 1.9M examples of their occurrences across film, television, and literature. We automatically score the {``}genderedness{''} of each trope in our TVTROPES dataset, which enables an analysis of (1) highly-gendered topics within tropes, (2) the relationship between gender bias and popular reception, and (3) how the gender of a work{'}s creator correlates with the types of tropes that they use.",
}
```

## Data samples

### film_imdb_match
|      |       Title        |       Trope        |      Example       |     CleanTitle     | tconst  |trope_id|title_id|
|------|--------------------|--------------------|--------------------|--------------------|---------|--------|--------|
|584615|TheGreatestShowOn...|ItsAllMyFault       |  Holly blames he...|thegreatestshowon...|tt0044672|t11922  |f13212  |
|157973|DoubleHarness       |TheReveal           | Joan tricked Joh...|doubleharness       |tt0023960|t23423  |f3550   |
|239952|HeartsOfDarknessA...|LifeImitatesArt     | The documentary ...|heartsofdarknessa...|tt0102015|t12858  |f5396   |
|257511|HowToTrainYourDra...|BoringInsult        | Referenced; Hicc...|howtotrainyourdra...|tt1646971|t02651  |f5803   |
|560066|TheDarkKnightRises  |SequelDisplacement  | Downplayed with ...|thedarkknightrises  |tt1345836|t19847  |f12644  |
|221031|GoneGirl            |TechnologyMarchesOn | Shooting films o...|gonegirl            |tt2267998|t22391  |f4995   |
|545152|TheBookOfEli        |MilesToGoBeforeIS...| In The Book of E...|thebookofeli        |tt1037705|t14122  |f12286  |
|103778|CasinoRoyale2006    |WackyWaysideTribe   | A variation occu...|casinoroyale2006    |tt0381061|t25452  |f2238   |
|326503|LordOfWar           |WarIsHell           | Those who suffer...|lordofwar           |tt0399295|t25547  |f7348   |
|565976|TheDuchess          |TheTheTitle         | The Duchess        |theduchess          |tt0864761|t23569  |f12796  |

### film_tropes
|      |       Title        |       Trope        |      Example       |trope_id|title_id|
|------|--------------------|--------------------|--------------------|--------|--------|
|570728|TheFan              |TheTheTitle         | The Fan            |t23569  |f12916  |
|45611 |AvengersInfinityWar |Jossed              | Marvel Cinematic...|t12127  |f1027   |
|55227 |BatmanBegins        |SoftGlass           | The Dark Knight ...|t20790  |f1197   |
|55513 |BatmanBegins        |ItIsBeyondSaving    | As stated by the...|t11906  |f1197   |
|259789|IHeartHuckabees     |OpposedMentors      | Philosophically ...|t16302  |f5885   |
|563212|TheDeathsOfIanStone |MySpeciesDothProt...| The Deaths of Ia...|t14904  |f12692  |
|661142|TheStepfather       |VeryLooselyBasedO...| The inspiration ...|t25182  |f14882  |
|452058|ScoobyDooMusicOfT...|TakeThat            | Daphne and Velma...|t22219  |f10422  |
|414934|QuickChange         |IndyPloy            | Fortunately, Gri...|t11355  |f9612   |
|605187|TheLastSamurai      |WaterfallShower     | Nathan comes acr...|t25594  |f13694  |

### genderedness_filtered
|       Trope        |   Gender Ratio    |Tokens|FemaleTokens|MaleTokens|       Corpus       |Normalized Gender Ratio|TotalMFTokens|     TokenRatio     |
|--------------------|-------------------|------|------------|----------|--------------------|-----------------------|-------------|--------------------|
|GodOfGods           |0.07650127974738415|2763  |5           |215       | in a setting wit...|-0.9535353505968780    |220          |0.079623597536025210|
|CaptainColorbeard   |0.11810722355618752|1020  |2           |55        |probably as a res...|-0.9282651120002727    |57           |0.055882352935697810|
|TheTropeKid         |0.09900163152562196|1143  |1           |33        |in the wild west ...|-0.9398692921953062    |34           |0.029746281712183176|
|TheDeadRiseToAdve...|0.00000000000000000|1503  |0           |24        |there was a point...|-1.0000000000000000    |24           |0.015968063871193077|
|CouncilOfAngels     |0.05518124442745930|1658  |1           |60        |the problem with ...|-0.9664845191555433    |61           |0.036791314834934176|
|DoubleStandardVio...|0.06600109415444158|1209  |1           |50        |it seems very com...|-0.9599128575334266    |51           |0.042183622825294980|
|EvolutionPowerUp    |0.00000000000000000|1604  |0           |47        |when something or...|-1.0000000000000000    |47           |0.029301745634083432|
|SuperSentaiStance   |0.12021625927588820|1264  |1           |27        |this is performed...|-0.9269841451247101    |28           |0.022151898732424690|
|WeaponsOfTheirTrade |0.08209891807068978|1005  |1           |40        |a specific style ...|-0.9501355080970305    |41           |0.040796019896438210|
|TheAllegedHouse     |0.08209891807068978|1677  |1           |40        | so a character j...|-0.9501355080970305    |41           |0.024448419795799137|

### lit_goodreads_match
|      |       Title        |       Trope        |      Example       |     CleanTitle     |       author       |verified_gender|title_id|trope_id|
|------|--------------------|--------------------|--------------------|--------------------|--------------------|---------------|--------|--------|
|188809|TheHitchhikersGui...|Panspermia          | The Hitchhiker's...|thehitchhikersgui...|Douglas Adams       |male           |lit11735|t16621  |
|352675|TheYearling         |ShootTheDog         | Ory does, but be...|theyearling         |Marjorie Kinnan R...|female         |lit14099|t20162  |
|268330|LastManStanding     |DidNotGetTheGuy     | Claire clearly w...|lastmanstanding     |David Baldacci      |male           |lit5827 |t27195  |
|328992|TheFriendsOfEddie...|DeathByIrony        | The ultimate fat...|thefriendsofeddie...|George V. Higgins   |male           |lit11367|t05271  |
|105688|TalesOfTheFiveHun...|LiteralGenie        | In the Mercedes ...|talesofthefivehun...|Mercedes Lackey     |female         |lit9895 |t12970  |
|268142|WomenInLove         |FriendToAllLiving...| Gudrun has this ...|womeninlove         |D.H. Lawrence       |male           |lit15279|t08611  |
|26546 |Discworld           |PermanentElectedO...| Late Jim Cloop, ...|discworld           |Terry Pratchett     |male           |lit2804 |t16862  |
|116830|BitingTheSun        |BodyBackupDrive     | Everyone in the ...|bitingthesun        |Tanith Lee          |female         |lit1261 |t02560  |
|109767|BeautyAndTheBeast   |TheZelig            | In Once Upon a T...|beautyandthebeast   |Jenni James         |female         |lit1131 |t29367  |
|192813|ThePostmanAlwaysR...|BettyAndVeronica    | A version that b...|thepostmanalwaysr...|James M. Cain       |male           |lit12796|t02154  |

### lit_tropes
|      |       Title        |      Trope       |      Example       |trope_id|title_id|
|------|--------------------|------------------|--------------------|--------|--------|
|396695|SixGunSnowWhite     |AdultsAreUseless  | Because none of ...|t00330  |lit9089 |
|183214|GentlemanBastard    |FeedTheMole       | Gentleman Bastar...|t07855  |lit4031 |
|262733|KingdomOfLittleWo...|RoyalBlood        | Important for po...|t19105  |lit5631 |
|675680|Worldwar            |FreudianTrio      | the three most s...|t08567  |lit15330|
|671819|WitchAndWizard      |MagicWand         | Witch & Wizard -...|t13559  |lit15221|
|22603 |Airman              |BlindMusician     | Linus Wynter.      |t02472  |lit456  |
|106633|DarkestPowers       |ApocalypseMaiden  | Margaret  looks ...|t01137  |lit2458 |
|235051|IfWeWereVillains    |ThereIsOnlyOneBed | When James comes...|t23409  |lit4999 |
|55743 |Berserker           |HumanityIsSuperior| In Fred Saberhag...|t10685  |lit1187 |
|81605 |Charly              |OppositesAttract  | Paul, who studie...|t16306  |lit1853 |

### tropes
|     |TropeID|       Trope        |    Description     |
|-----|-------|--------------------|--------------------|
|14949|t14950 |NailEm              | Nail guns are a ...|
|14579|t14580 |MostGamersAreMale   |This trope holds ...|
|14085|t14086 |MidairCollision     |So you have a bun...|
|26985|t26986 |OffScreenMomentOf...| Something big is...|
|13189|t13190 |LoserFriendPuzzle...|Some people are o...|
|26927|t26928 |SpearCounterpart    | One common metho...|
|13529|t13530 |MagicHair           |This page covers ...|
|26522|t26523 |YouMeddlingKids     | When the evil ch...|
|4727 |t04728 |CreepyCoolCrosses   |Most Japanese are...|
|17837|t17838 |ProtectionFromEdi...|(This writer can'...|

### tv_imdb_match
|      |       Title        |       Trope        |      Example       |     CleanTitle     | tconst  |trope_id|title_id|
|------|--------------------|--------------------|--------------------|--------------------|---------|--------|--------|
|22299 |AvengerPenguins     |ComicalOverreacting | The episode "Bea...|avengerpenguins     |tt0481434|t04131  |tv377   |
|395560|TheDreamstone       |ComicallyLopsided...| Basing itself he...|thedreamstone       |tt0299286|t04126  |tv6098  |
|1697  |AbsalonsHemmelighed |TheGloriousWarOfS...| Subverted. With ...|absalonshemmelighed |tt0929638|t22931  |tv63    |
|186926|JAG                 |ICouldABeenAConte...| JAG: Bud's colle...|jag                 |tt0112022|t27383  |tv2866  |
|91333 |Defiance            |AwesomeDearBoy      | Nicole Munoz say...|defiance            |tt2189221|t01599  |tv1455  |
|181722|IceFantasy          |ImmortalityBegins...| Or maybe 30. Ka ...|icefantasy          |tt5022298|t11124  |tv2723  |
|346693|StarTrekTheNextGe...|ProudWarriorRaceGuys| The first two bo...|startrekthenextge...|tt0092455|t30554  |tv5461  |
|227860|MagnificentCentury  |WasItAllALie        | After Sadika bre...|magnificentcentury  |tt1848220|t25574  |tv3529  |
|412829|TheLateShow1992     |UnusualEuphemism    | "Financial Advic...|thelateshow1992     |tt0103468|t24977  |tv6457  |
|440578|TheTwilightZone1959 |BarredFromTheAfte...| In the The Twili...|thetwilightzone1959 |tt0052520|t01869  |tv7004  |

### tv_tropes
|      |      Title      |       Trope        |      Example       |trope_id|title_id|
|------|-----------------|--------------------|--------------------|--------|--------|
|70722 |Chespirito       |ShaggyDogStory      | The Cyrano de Be...|t20004  |tv1051  |
|159405|HamishMacbeth    |OpposingSportsTeam  | Dunbracken in th...|t16304  |tv2391  |
|457324|TonganNinja      |InsistentTerminology| Never mind the f...|t11527  |tv7244  |
|59250 |BustedKorea      |CompetitionFreak    | Sehun,  big time...|t04199  |tv877   |
|146010|GameOfThrones    |PostRapeTaunt       | In Game of Thron...|t17456  |tv2143  |
|157831|Grimm            |PoisonedWeapons     | Monroe uses an e...|t17304  |tv2346  |
|120131|ErkyPerky        |ExpositoryThemeTune | The theme song e...|t07305  |tv1803  |
|313687|SaturdayNightLive|AttentionDeficitO...| In the '80s, Sat...|t29900  |tv5018  |
|43438 |BoardwalkEmpire  |HollywoodHypeMachine| Gretchen Mol was...|t10402  |tv710   |
|272149|OrphanBlack      |WinBackTheCrowd     | Orphan Black als...|t28118  |tv4266  |
