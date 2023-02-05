# === Your task ==============================================================
# Let's have some 'fun'.
# Go to http://en.wikipedia.org/wiki/Garden_path_sentence and have a brief read at what a 'Garden Path sentence' is (at the top) and look at the 'Examples'

import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# Source: https://www.apartmenttherapy.com/garden-sentences-262915 and https://en.wikipedia.org/wiki/Garden-path_sentence

garden_path_sentence1 = "The horse raced past the barn fell."
garden_path_sentence2 = "The old man the boat."
garden_path_sentence3 = "The florist sent the flowers was pleased."
garden_path_sentence4 = "The cotton clothing is made of grows in Mississippi."
garden_path_sentence5 = "The sour drink from the ocean."
garden_path_sentence6 = "Have the students who failed the exam take the supplementary."
garden_path_sentence7 = "We painted the wall with cracks."
garden_path_sentence8 = "The man who hunts ducks out on weekends."
garden_path_sentence9 = "The raft floated down the river sank."
garden_path_sentence10 = "When Fred eats food gets thrown."
garden_path_sentence11 = "Mary gave the child the dog bit a Band-Aid."
garden_path_sentence12 = "The girl told the story cried."
garden_path_sentence13 = "I convinced her children are noisy."
garden_path_sentence14 = "Helen is expecting tomorrow to be a bad day."
garden_path_sentence15 = "Fat people eat accumulates."
garden_path_sentence16 = "I know the words to that song about the queen don’t rhyme."
garden_path_sentence17 = "She told me a little white lie will come back to haunt me."
garden_path_sentence18 = "The dog that I had really loved bones."
garden_path_sentence19 = "That Jill is never here hurts."
garden_path_sentence20 = "The man who whistles tunes pianos."
garden_path_sentence21 = "The complex houses married and single soldiers and their families."


# 2. Tokenise and perform Entity recognition for each of the sentences after you have stored them in a list called gardenpathSentences.

gardenpathSentences = [
                    garden_path_sentence1, garden_path_sentence2, garden_path_sentence3, garden_path_sentence4, garden_path_sentence5,
                    garden_path_sentence6, garden_path_sentence7, garden_path_sentence8, garden_path_sentence9, garden_path_sentence10,
                    garden_path_sentence11, garden_path_sentence12, garden_path_sentence13, garden_path_sentence14, garden_path_sentence15,
                    garden_path_sentence16, garden_path_sentence17, garden_path_sentence18, garden_path_sentence19, garden_path_sentence20, 
                    garden_path_sentence21]

for number, sentence in enumerate(gardenpathSentences):
    sentence_with_number = f"sentence nr {number + 1}"
    tokenise_garden_path_sentence = nlp(sentence)
    print(f"Tokens in {sentence_with_number}:\n")
    print([(token, token.orth_, token.orth) for token in tokenise_garden_path_sentence])
    print(f"\nEntities in {sentence_with_number}:\n")
    print([(entity, entity.label_, entity.label) for entity in tokenise_garden_path_sentence.ents])
    print()

# 3. See how spaCy has categorised these sentences and look up the entities you don't understand
 
# Result:
  
"""Tokens in sentence nr 1:

[(The, 'The', 5059648917813135842), (horse, 'horse', 9866490340549498003), (raced, 'raced', 11985977600559752646), (past, 'past', 14080206577736366893), (the, 'the', 7425985699627899538), (barn, 'barn', 1731024304121373681), (fell, 'fell', 17406646348554510309), (., '.', 12646065887601541794)]

Entities in sentence nr 1:

[]

Tokens in sentence nr 2:

[(The, 'The', 5059648917813135842), (old, 'old', 2483095116303079762), (man, 'man', 3104811030673030468), (the, 'the', 7425985699627899538), (boat, 'boat', 11387929873876272110), (., '.', 12646065887601541794)]

Entities in sentence nr 2:

[]

Tokens in sentence nr 3:

[(The, 'The', 5059648917813135842), (florist, 'florist', 10501838060908119271), (sent, 'sent', 16056986141218963985), (the, 'the', 7425985699627899538), (flowers, 'flowers', 2477902471846530091), (was, 'was', 9921686513378912864), (pleased, 'pleased', 4426875666208874359), (., '.', 12646065887601541794)]

Entities in sentence nr 3:

[]

Tokens in sentence nr 4:

[(The, 'The', 5059648917813135842), (cotton, 'cotton', 13158503143813622304), (clothing, 'clothing', 11978358972660538478), (is, 'is', 3411606890003347522), (made, 'made', 
7136294487848412980), (of, 'of', 886050111519832510), (grows, 'grows', 6115445568100627063), (in, 'in', 3002984154512732771), (Mississippi, 'Mississippi', 1946980641541756374), (., '.', 12646065887601541794)]

Entities in sentence nr 4:

[(Mississippi, 'GPE', 384)]

Tokens in sentence nr 5:

[(The, 'The', 5059648917813135842), (sour, 'sour', 1437310558085749269), (drink, 'drink', 8799542030263951485), (from, 'from', 7831658034963690409), (the, 'the', 7425985699627899538), (ocean, 'ocean', 11641983324036055121), (., '.', 12646065887601541794)]   

Entities in sentence nr 5:

[]

Tokens in sentence nr 6:

[(Have, 'Have', 14832259926261516629), (the, 'the', 7425985699627899538), (students, 'students', 7876819095232981007), (who, 'who', 3876862883474502309), (failed, 'failed', 4500079622559289248), (the, 'the', 7425985699627899538), (exam, 'exam', 9704506296879342145), (take, 'take', 6789454535283781228), (the, 'the', 7425985699627899538), (supplementary, 'supplementary', 7472160464603105822), (., '.', 12646065887601541794)]     

Entities in sentence nr 6:

[]

Tokens in sentence nr 7:

[(We, 'We', 15667417291854480293), (painted, 'painted', 17889146272910524500), (the, 'the', 7425985699627899538), (wall, 'wall', 14432890480967458232), (with, 'with', 12510949447758279278), (cracks, 'cracks', 2407019867429134975), (., '.', 12646065887601541794)]

Entities in sentence nr 7:

[]

Tokens in sentence nr 8:

[(The, 'The', 5059648917813135842), (man, 'man', 3104811030673030468), (who, 'who', 3876862883474502309), (hunts, 'hunts', 8400608406397654257), (ducks, 'ducks', 5423654250641619862), (out, 'out', 1696981056005371314), (on, 'on', 5640369432778651323), (weekends, 'weekends', 6848325044638967861), (., '.', 12646065887601541794)]

Entities in sentence nr 8:

[]

Tokens in sentence nr 9:

[(The, 'The', 5059648917813135842), (raft, 'raft', 7154368781129989833), (floated, 'floated', 1678793496730311555), (down, 'down', 6421409113692203669), (the, 'the', 7425985699627899538), (river, 'river', 9103378528718840401), (sank, 'sank', 8128172682333265657), (., '.', 12646065887601541794)]

Entities in sentence nr 9:

[]

Tokens in sentence nr 10:

[(When, 'When', 10109588199364727116), (Fred, 'Fred', 9019830820092895125), (eats, 'eats', 12912699194130420726), (food, 'food', 18057327756930201825), (gets, 'gets', 15696715460206213879), (thrown, 'thrown', 8893083121554436667), (., '.', 12646065887601541794)]

Entities in sentence nr 10:

[]

Tokens in sentence nr 11:

[(Mary, 'Mary', 10580883238578074496), (gave, 'gave', 4776877220522498379), (the, 'the', 7425985699627899538), (child, 'child', 737253710922290542), (the, 'the', 7425985699627899538), (dog, 'dog', 7562983679033046312), (bit, 'bit', 1794436035373472204), (a, 
'a', 11901859001352538922), (Band, 'Band', 3274553646799644611), (-, '-', 9153284864653046197), (Aid, 'Aid', 4475664174047812614), (., '.', 12646065887601541794)]

Entities in sentence nr 11:

[(Mary, 'PERSON', 380)]

Tokens in sentence nr 12:

[(The, 'The', 5059648917813135842), (girl, 'girl', 3995049128985859847), (told, 'told', 1245643389253732868), (the, 'the', 7425985699627899538), (story, 'story', 5345497848075657444), (cried, 'cried', 18384085136260030139), (., '.', 12646065887601541794)]   

Entities in sentence nr 12:

[]

Tokens in sentence nr 13:

[(I, 'I', 4690420944186131903), (convinced, 'convinced', 2177692269620059649), (her, 'her', 4115755726172261197), (children, 'children', 2413477756209127936), (are, 'are', 
5012629990875267006), (noisy, 'noisy', 5527247695594041383), (., '.', 12646065887601541794)]

Entities in sentence nr 13:

[]

Tokens in sentence nr 14:

[(Helen, 'Helen', 8987078322310499664), (is, 'is', 3411606890003347522), (expecting, 'expecting', 6313445122590802307), (tomorrow, 'tomorrow', 3573583789758258062), (to, 'to', 3791531372978436496), (be, 'be', 10382539506755952630), (a, 'a', 11901859001352538922), (bad, 'bad', 12342627399458421040), (day, 'day', 1608482186128794349), (., '.', 
12646065887601541794)]

Entities in sentence nr 14:

[(tomorrow, 'DATE', 391), (a bad day, 'DATE', 391)]

Tokens in sentence nr 15:

[(Fat, 'Fat', 15171857674657094662), (people, 'people', 7593739049417968140), (eat, 'eat', 9837207709914848172), (accumulates, 'accumulates', 334484709300502388), (., '.', 
12646065887601541794)]

Entities in sentence nr 15:

[]

Tokens in sentence nr 16:

[(I, 'I', 4690420944186131903), (know, 'know', 7743033266031195906), (the, 'the', 7425985699627899538), (words, 'words', 10289140944597012527), (to, 'to', 3791531372978436496), (that, 'that', 4380130941430378203), (song, 'song', 9688994450605453460), (about, 'about', 942632335873952620), (the, 'the', 7425985699627899538), (queen, 'queen', 4176741725343376093), (do, 'do', 2158845516055552166), (n’t, 'n’t', 16712971838599463365), (rhyme, 'rhyme', 1102661262456909351), (., '.', 12646065887601541794)]

Entities in sentence nr 16:

[]

Tokens in sentence nr 17:

[(She, 'She', 5252949303365547547), (told, 'told', 1245643389253732868), (me, 'me', 18197037023634208128), (a, 'a', 11901859001352538922), (little, 'little', 9778055143417507723), (white, 'white', 16857069738040043275), (lie, 'lie', 4613777942946297274), (will, 'will', 18307573501153647118), (come, 'come', 5307304325359566725), (back, 'back', 15255859468896132977), (to, 'to', 3791531372978436496), (haunt, 'haunt', 14648922648205441880), (me, 'me', 18197037023634208128), (., '.', 12646065887601541794)]

Entities in sentence nr 17:

[]

Tokens in sentence nr 18:

[(The, 'The', 5059648917813135842), (dog, 'dog', 7562983679033046312), (that, 'that', 
4380130941430378203), (I, 'I', 4690420944186131903), (had, 'had', 12960022596163002503), (really, 'really', 14653600329166397554), (loved, 'loved', 14704622115168303900), (bones, 'bones', 2051171804970710217), (., '.', 12646065887601541794)]

Entities in sentence nr 18:

[]

Tokens in sentence nr 19:

[(That, 'That', 4759254855483594167), (Jill, 'Jill', 3047967728500374997), (is, 'is', 
3411606890003347522), (never, 'never', 10879546028211794123), (here, 'here', 411390626470654571), (hurts, 'hurts', 13935874261429573119), (., '.', 12646065887601541794)]   

Entities in sentence nr 19:

[(Jill, 'PERSON', 380)]

Tokens in sentence nr 20:

[(The, 'The', 5059648917813135842), (man, 'man', 3104811030673030468), (who, 'who', 3876862883474502309), (whistles, 'whistles', 13456737561780874747), (tunes, 'tunes', 1274938788288672369), (pianos, 'pianos', 13877332455828461807), (., '.', 12646065887601541794)]

Entities in sentence nr 20:

[]

Tokens in sentence nr 21:

[(The, 'The', 5059648917813135842), (complex, 'complex', 11125307656307208867), (houses, 'houses', 12236405033243632862), (married, 'married', 15974428657194256046), (and, 
'and', 2283656566040971221), (single, 'single', 9644341664820045211), (soldiers, 'soldiers', 13157451586059593190), (and, 'and', 2283656566040971221), (their, 'their', 4244585616942201722), (families, 'families', 13150649422924114104), (., '.', 12646065887601541794)]

Entities in sentence nr 21:

[]
    
"""


# 4. At the bottom of your file, write a comment about two unusual entities you found that spaCy gave one of the words of your sentences - did you expect this?

# Comment:
# There were either no entities or if there were then they were not unusual.