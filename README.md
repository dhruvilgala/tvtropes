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
|      |                Title                |        Trope        |                Example                 |             CleanTitle              | tconst  |trope_id|title_id|
|------|-------------------------------------|---------------------|----------------------------------------|-------------------------------------|---------|--------|--------|
|584615|TheGreatestShowOnEarth               |ItsAllMyFault        |  Holly blames herself for Sebastian'...|thegreatestshowonearth               |tt0044672|t11922  |f13212  |
|157973|DoubleHarness                        |TheReveal            | Joan tricked John into marrying her ...|doubleharness                        |tt0023960|t23423  |f3550   |
|239952|HeartsOfDarknessAFilmmakersApocalypse|LifeImitatesArt      | The documentary points out several p...|heartsofdarknessafilmmakersapocalypse|tt0102015|t12858  |f5396   |
|257511|HowToTrainYourDragon2                |BoringInsult         | Referenced; Hiccup   It's not every ...|howtotrainyourdragon2                |tt1646971|t02651  |f5803   |
|560066|TheDarkKnightRises                   |SequelDisplacement   | Downplayed with The Dark Knight Tril...|thedarkknightrises                   |tt1345836|t19847  |f12644  |
|221031|GoneGirl                             |TechnologyMarchesOn  | Shooting films on, uh, film, pretty ...|gonegirl                             |tt2267998|t22391  |f4995   |
|545152|TheBookOfEli                         |MilesToGoBeforeISleep| In The Book of Eli, Eli is on a Miss...|thebookofeli                         |tt1037705|t14122  |f12286  |
|103778|CasinoRoyale2006                     |WackyWaysideTribe    | A variation occurs in the James Bond...|casinoroyale2006                     |tt0381061|t25452  |f2238   |
|326503|LordOfWar                            |WarIsHell            | Those who suffer in war are rarely t...|lordofwar                            |tt0399295|t25547  |f7348   |
|565976|TheDuchess                           |TheTheTitle          | The Duchess                            |theduchess                           |tt0864761|t23569  |f12796  |

### film_tropes
|      |          Title           |           Trope            |                Example                 |trope_id|title_id|
|------|--------------------------|----------------------------|----------------------------------------|--------|--------|
|570728|TheFan                    |TheTheTitle                 | The Fan                                |t23569  |f12916  |
|45611 |AvengersInfinityWar       |Jossed                      | Marvel Cinematic Universe:  Iron Man...|t12127  |f1027   |
|55227 |BatmanBegins              |SoftGlass                   | The Dark Knight Trilogy:  This must ...|t20790  |f1197   |
|55513 |BatmanBegins              |ItIsBeyondSaving            | As stated by the page quotation, thi...|t11906  |f1197   |
|259789|IHeartHuckabees           |OpposedMentors              | Philosophically opposed existential ...|t16302  |f5885   |
|563212|TheDeathsOfIanStone       |MySpeciesDothProtestTooMuch | The Deaths of Ian Stone ups the ante...|t14904  |f12692  |
|661142|TheStepfather             |VeryLooselyBasedOnATrueStory| The inspiration for the series was m...|t25182  |f14882  |
|452058|ScoobyDooMusicOfTheVampire|TakeThat                    | Daphne and Velma are fans of " Silve...|t22219  |f10422  |
|414934|QuickChange               |IndyPloy                    | Fortunately, Grimm is good at  Xanat...|t11355  |f9612   |
|605187|TheLastSamurai            |WaterfallShower             | Nathan comes across his host (the wi...|t25594  |f13694  |

### genderedness_filtered
|              Trope               |   Gender Ratio    |Tokens|FemaleTokens|MaleTokens|                 Corpus                 |Normalized Gender Ratio|TotalMFTokens|     TokenRatio     |
|----------------------------------|-------------------|------|------------|----------|----------------------------------------|-----------------------|-------------|--------------------|
|GodOfGods                         |0.07650127974738415|2763  |5           |215       | in a setting with a few or more gods...|-0.9535353505968780    |220          |0.079623597536025210|
|CaptainColorbeard                 |0.11810722355618752|1020  |2           |55        |probably as a result of infamous sail...|-0.9282651120002727    |57           |0.055882352935697810|
|TheTropeKid                       |0.09900163152562196|1143  |1           |33        |in the wild west a man had to grow up...|-0.9398692921953062    |34           |0.029746281712183176|
|TheDeadRiseToAdvertise            |0.00000000000000000|1503  |0           |24        |there was a point when the uncanny va...|-1.0000000000000000    |24           |0.015968063871193077|
|CouncilOfAngels                   |0.05518124442745930|1658  |1           |60        |the problem with god is that his give...|-0.9664845191555433    |61           |0.036791314834934176|
|DoubleStandardViolenceChildOnAdult|0.06600109415444158|1209  |1           |50        |it seems very common for writers to l...|-0.9599128575334266    |51           |0.042183622825294980|
|EvolutionPowerUp                  |0.00000000000000000|1604  |0           |47        |when something or someone transforms ...|-1.0000000000000000    |47           |0.029301745634083432|
|SuperSentaiStance                 |0.12021625927588820|1264  |1           |27        |this is performed by a team usually i...|-0.9269841451247101    |28           |0.022151898732424690|
|WeaponsOfTheirTrade               |0.08209891807068978|1005  |1           |40        |a specific style of improvised weapon...|-0.9501355080970305    |41           |0.040796019896438210|
|TheAllegedHouse                   |0.08209891807068978|1677  |1           |40        | so a character just bought a new hou...|-0.9501355080970305    |41           |0.024448419795799137|

### lit_goodreads_match
|      |            Title             |         Trope          |                Example                 |          CleanTitle          |         author         |verified_gender|title_id|trope_id|
|------|------------------------------|------------------------|----------------------------------------|------------------------------|------------------------|---------------|--------|--------|
|188809|TheHitchhikersGuideToTheGalaxy|Panspermia              | The Hitchhiker's Guide to the Galaxy...|thehitchhikersguidetothegalaxy|Douglas Adams           |male           |lit11735|t16621  |
|352675|TheYearling                   |ShootTheDog             | Ory does, but being a poor shot, she...|theyearling                   |Marjorie Kinnan Rawlings|female         |lit14099|t20162  |
|268330|LastManStanding               |DidNotGetTheGuy         | Claire clearly wants to get with Web...|lastmanstanding               |David Baldacci          |male           |lit5827 |t27195  |
|328992|TheFriendsOfEddieCoyle        |DeathByIrony            | The ultimate fate of   Eddie Coyle ,...|thefriendsofeddiecoyle        |George V. Higgins       |male           |lit11367|t05271  |
|105688|TalesOfTheFiveHundredKingdoms |LiteralGenie            | In the Mercedes Lackey book One Good...|talesofthefivehundredkingdoms |Mercedes Lackey         |female         |lit9895 |t12970  |
|268142|WomenInLove                   |FriendToAllLivingThings | Gudrun has this tendency.              |womeninlove                   |D.H. Lawrence           |male           |lit15279|t08611  |
|26546 |Discworld                     |PermanentElectedOfficial| Late Jim Cloop, the mayor of Scrote ...|discworld                     |Terry Pratchett         |male           |lit2804 |t16862  |
|116830|BitingTheSun                  |BodyBackupDrive         | Everyone in the cities in Biting the...|bitingthesun                  |Tanith Lee              |female         |lit1261 |t02560  |
|109767|BeautyAndTheBeast             |TheZelig                | In Once Upon a Time, Rumpelstiltskin...|beautyandthebeast             |Jenni James             |female         |lit1131 |t29367  |
|192813|ThePostmanAlwaysRingsTwice    |BettyAndVeronica        | A version that became popularized in...|thepostmanalwaysringstwice    |James M. Cain           |male           |lit12796|t02154  |

### lit_tropes
|      |        Title        |      Trope       |                Example                 |trope_id|title_id|
|------|---------------------|------------------|----------------------------------------|--------|--------|
|396695|SixGunSnowWhite      |AdultsAreUseless  | Because none of the servants want to...|t00330  |lit9089 |
|183214|GentlemanBastard     |FeedTheMole       | Gentleman Bastard: The Republic of T...|t07855  |lit4031 |
|262733|KingdomOfLittleWounds|RoyalBlood        | Important for politics in The Kingdo...|t19105  |lit5631 |
|675680|Worldwar             |FreudianTrio      | the three most senior members of the...|t08567  |lit15330|
|671819|WitchAndWizard       |MagicWand         | Witch & Wizard - Wisty has an old dr...|t13559  |lit15221|
|22603 |Airman               |BlindMusician     | Linus Wynter.                          |t02472  |lit456  |
|106633|DarkestPowers        |ApocalypseMaiden  | Margaret  looks at  Chloe  this way ...|t01137  |lit2458 |
|235051|IfWeWereVillains     |ThereIsOnlyOneBed | When James comes to visit Oliver in ...|t23409  |lit4999 |
|55743 |Berserker            |HumanityIsSuperior| In Fred Saberhagen's Berserker novel...|t10685  |lit1187 |
|81605 |Charly               |OppositesAttract  | Paul, who studies physics, falls in ...|t16306  |lit1853 |

### tropes
|     |TropeID|           Trope           |              Description               |
|-----|-------|---------------------------|----------------------------------------|
|14949|t14950 |NailEm                     | Nail guns are a common Improvised We...|
|14579|t14580 |MostGamersAreMale          |This trope holds that the primary dem...|
|14085|t14086 |MidairCollision            |So you have a bunch of flying things,...|
|26985|t26986 |OffScreenMomentOfAwesome   | Something big is about to go down. E...|
|13189|t13190 |LoserFriendPuzzlesOutsiders|Some people are obviously important. ...|
|26927|t26928 |SpearCounterpart           | One common method used in creating a...|
|13529|t13530 |MagicHair                  |This page covers hair that has magica...|
|26522|t26523 |YouMeddlingKids            | When the evil character is finally b...|
|4727 |t04728 |CreepyCoolCrosses          |Most Japanese are not Christian. They...|
|17837|t17838 |ProtectionFromEditors      |(This writer can't be blocked, target...|

### tv_imdb_match
|      |          Title          |             Trope             |                Example                 |       CleanTitle        | tconst  |trope_id|title_id|
|------|-------------------------|-------------------------------|----------------------------------------|-------------------------|---------|--------|--------|
|22299 |AvengerPenguins          |ComicalOverreacting            | The episode "Beauties and the Beasts...|avengerpenguins          |tt0481434|t04131  |tv377   |
|395560|TheDreamstone            |ComicallyLopsidedRivalry       | Basing itself heavily on Golden Age ...|thedreamstone            |tt0299286|t04126  |tv6098  |
|1697  |AbsalonsHemmelighed      |TheGloriousWarOfSisterlyRivalry| Subverted. With their sharp personal...|absalonshemmelighed      |tt0929638|t22931  |tv63    |
|186926|JAG                      |ICouldABeenAContender          | JAG: Bud's college roommate Ron Katz...|jag                      |tt0112022|t27383  |tv2866  |
|91333 |Defiance                 |AwesomeDearBoy                 | Nicole Munoz says she does a lot of ...|defiance                 |tt2189221|t01599  |tv1455  |
|181722|IceFantasy               |ImmortalityBeginsAtTwenty      | Or maybe 30. Ka Suo and Shi and thei...|icefantasy               |tt5022298|t11124  |tv2723  |
|346693|StarTrekTheNextGeneration|ProudWarriorRaceGuys           | The first two books of the Star Trek...|startrekthenextgeneration|tt0092455|t30554  |tv5461  |
|227860|MagnificentCentury       |WasItAllALie                   | After Sadika breaks her facade and  ...|magnificentcentury       |tt1848220|t25574  |tv3529  |
|412829|TheLateShow1992          |UnusualEuphemism               | "Financial Advice", used in referenc...|thelateshow1992          |tt0103468|t24977  |tv6457  |
|440578|TheTwilightZone1959      |BarredFromTheAfterlife         | In the The Twilight Zone (1959) epis...|thetwilightzone1959      |tt0052520|t01869  |tv7004  |

### tv_tropes
|      |      Title      |         Trope         |                Example                 |trope_id|title_id|
|------|-----------------|-----------------------|----------------------------------------|--------|--------|
|70722 |Chespirito       |ShaggyDogStory         | The Cyrano de Bergerac skit. Cyrano ...|t20004  |tv1051  |
|159405|HamishMacbeth    |OpposingSportsTeam     | Dunbracken in the  Shinty Episode   ...|t16304  |tv2391  |
|457324|TonganNinja      |InsistentTerminology   | Never mind the fact that they never ...|t11527  |tv7244  |
|59250 |BustedKorea      |CompetitionFreak       | Sehun,  big time . He uses up all of...|t04199  |tv877   |
|146010|GameOfThrones    |PostRapeTaunt          | In Game of Thrones, Brienne and Jaim...|t17456  |tv2143  |
|157831|Grimm            |PoisonedWeapons        | Monroe uses an elephant gun with bul...|t17304  |tv2346  |
|120131|ErkyPerky        |ExpositoryThemeTune    | The theme song explains the entire p...|t07305  |tv1803  |
|313687|SaturdayNightLive|AttentionDeficitOhShiny| In the '80s, Saturday Night Live had...|t29900  |tv5018  |
|43438 |BoardwalkEmpire  |HollywoodHypeMachine   | Gretchen Mol was touted as another "...|t10402  |tv710   |
|272149|OrphanBlack      |WinBackTheCrowd        | Orphan Black also seems to have rebo...|t28118  |tv4266  |
