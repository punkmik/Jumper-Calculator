# knitting gauge from swatching
# future - could make the variables be functions that calculate the stitches and rows per inch from a 4 inch input



### FUNCTIONS ###

# calculations
# cast on count: [back neck width x sts per inch] + [~30% of that number for sleeve top x 2] + [1 front neck st x 2] = CO
#castoncountold = ( neckwidthinches * stitchesperinch ) + ( ( neckwidthinches * stitchesperinch * 0.3 ) * 2 ) + 2

def calcCastoncount( theneckwidthinches , thestitchesperinch ) :
	theCalculation = (theneckwidthinches * thestitchesperinch) + ((theneckwidthinches * thestitchesperinch * 0.3) * 2) + 2
	return theCalculation;



#Under arm cast on count - after separating sleeves
#desired underarm width (rule of thumb is ~8% of body circumference) x sts per inch = underarm CO count
#underarmcastoncountold = ( chestcircumferenceinches * 0.08 ) * stitchesperinch

def calcUnderarmcastoncount( thechestcircumferenceinches, thestitchesperinch ) :
	theCalculation = ( thechestcircumferenceinches * 0.08 ) * thestitchesperinch
	return theCalculation;



# neck depth: desired drop from back to front neck edge x rows per inch = neck depth
#neckdepthold = backtofrontneckdropinches * rowsperinch

def calcNeckdepth ( thebacktofrontneckdropinches , therowsperinch ) :
	theCalculation = ( thebacktofrontneckdropinches * therowsperinch )
	return theCalculation;


# front and back stitch count at underarm/chest:
#  1/2 chest circumference x sts per inch = front or back st count***
#NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping.
#frontandbackstitchcountchestold = ( chestcircumferenceinches / 2 ) * stitchesperinch - underarmcastoncount

def calcFrontandbackstitchcountchest ( thechestcircumferenceinches, thestitchesperinch, theunderarmcastoncount  ):
	theCalculation = ( thechestcircumferenceinches / 2 ) * thestitchesperinch - theunderarmcastoncount
	return theCalculation;


#sleeves stitch count:
#desired sleeve circumference x sts per inch = sleeve st count***
#NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping
#sleevestitchcountold = sleevecircumferenceinches * stitchesperinch - underarmcastoncount

def calcSleevestitchcount ( thesleevecircumferenceinches , thestitchesperinch ,  theunderarmcastoncount) :
	theCalculation = thesleevecircumferenceinches * thestitchesperinch - theunderarmcastoncount
	return theCalculation;


#Yoke depth
#desired distance from shoulder to underarm x rows/rounds per inch = yoke depth
#yokedepthold = shouldertounderaminches * rowsperinch

def calcYokedepth ( theshouldertounderaminches , therowsperinch ) :
	theCalculation = theshouldertounderaminches * therowsperinch
	return theCalculation;


#desired sleeve lenght: sleeve length x rows per inch
#sleevelengthold = sleevelenghtinches * rowsperinch

def calcSleevelenght ( thesleevelenghtinches , therowsperinch ) :
	theCalculation = thesleevelenghtinches * therowsperinch
	return theCalculation;



class PatternInputClass :
	stitchesperinch = 0
	rowsperinch = 0
	neckwidthinches = 0
	chestcircumferenceinches = 0
	backtofrontneckdropinches = 0
	sleevecircumferenceinches = 0
	shouldertounderaminches = 0
	sleevelenghtinches = 0


###   USER INPUT ###
def getPatternInputFromUser() :

	patternInput = PatternInputClass()

	patternInput.stitchesperinch = float( raw_input("Please enter your number of stitches per 1 inch: ") )
	patternInput.rowsperinch = float( raw_input("Please enter your number of rows per 1 inch: ") )


	# personal measurements

	patternInput.neckwidthinches = float( raw_input("Please enter your desired neck width: ") )

	patternInput.chestcircumferenceinches = float( raw_input("Please enter your desired chest circumference: ") )

	patternInput.backtofrontneckdropinches = float( raw_input("Please enter your desired neck depth: ") )

	patternInput.sleevecircumferenceinches = float( raw_input("Please enter your desired sleeve circumference: ") )

	patternInput.shouldertounderaminches = float( raw_input("Please enter your desired yoke depth: ") )

	patternInput.sleevelenghtinches = float( raw_input("Please enter your desired sleeve length: ") )

	return patternInput;


class Pattern :
	castoncount = 0
	underarmcastoncount = 0
	neckdepth = 0
	frontandbackstitchcountchest = 0
	sleevestitchcount = 0
	yokedepth = 0
	sleevelength = 0

### MAIN PART ###
def calcPattern(patternInput) :

	pattern = Pattern()

	pattern.castoncount = calcCastoncount(patternInput.neckwidthinches, patternInput.stitchesperinch)

	pattern.underarmcastoncount = calcUnderarmcastoncount(patternInput.chestcircumferenceinches, patternInput.stitchesperinch)

	pattern.neckdepth = calcNeckdepth(patternInput.backtofrontneckdropinches, patternInput.rowsperinch)

	pattern.frontandbackstitchcountchest = calcFrontandbackstitchcountchest (patternInput.chestcircumferenceinches, patternInput.stitchesperinch, pattern.underarmcastoncount)

	pattern.sleevestitchcount = calcSleevestitchcount(patternInput.sleevecircumferenceinches, patternInput.stitchesperinch, pattern.underarmcastoncount)

	pattern.yokedepth = calcYokedepth(patternInput.shouldertounderaminches, patternInput.rowsperinch)

	pattern.sleevelength = calcSleevelenght(patternInput.sleevelenghtinches, patternInput.rowsperinch)

	return pattern;


### OUTPUT ###
def printDebug( pattern ) :

	note_text = "You need to cast on %s stitches." % pattern.castoncount
	note_text += "\nYour under arm cast on count is %s stitches." % pattern.underarmcastoncount
	note_text += "\nYou need to knit %s rows for your desired neck depth." % pattern.neckdepth
	note_text += "\nYou need to increase to %s stitches for front and back." % pattern.frontandbackstitchcountchest
	note_text += "\nYou need to increase to %s sleeve stitches." % pattern.sleevestitchcount
	note_text += "\nYou need to knit %s rows for your desired yoke depth." % pattern.yokedepth
	note_text += "\nYou need to knit %s rows for your desired sleeve length." % pattern.sleevelength

	print note_text

	return;



def main() :
	patternInput = getPatternInputFromUser()
	pattern = calcPattern( patternInput )
	printDebug( pattern )


main()
