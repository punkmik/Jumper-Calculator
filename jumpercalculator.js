//knitting gauge from swatching
//future - could make the variables be functions that calculate the stitches and rows per inch from a 4 inch input



 //FUNCTIONS

//calculations
//cast on count: [back neck width x sts per inch] + [~30% of that number for sleeve top x 2] + [1 front neck st x 2] = CO
//castoncountold = ( neckwidthinches * stitchesperinch ) + ( ( neckwidthinches * stitchesperinch * 0.3 ) * 2 ) + 2

function calcCastoncount( theneckwidthinches , thestitchesperinch ) {
	theCalculation = (theneckwidthinches * thestitchesperinch) + ((theneckwidthinches * thestitchesperinch * 0.3) * 2) + 2
	return theCalculation;

	}

//Under arm cast on count - after separating sleeves
//desired underarm width (rule of thumb is ~8% of body circumference) x sts per inch = underarm CO count
//underarmcastoncountold = ( chestcircumferenceinches * 0.08 ) * stitchesperinch

function calcUnderarmcastoncount( thechestcircumferenceinches, thestitchesperinch ) {
	theCalculation = ( thechestcircumferenceinches * 0.08 ) * thestitchesperinch
	return theCalculation;

	}



//neck depth: desired drop from back to front neck edge x rows per inch = neck depth
//neckdepthold = backtofrontneckdropinches * rowsperinch

function calcNeckdepth ( thebacktofrontneckdropinches , therowsperinch ) {
	theCalculation = ( thebacktofrontneckdropinches * therowsperinch )
	return theCalculation;

	}


//front and back stitch count at underarm/chest:
//1/2 chest circumference x sts per inch = front or back st count***
//NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping.
//frontandbackstitchcountchestold = ( chestcircumferenceinches / 2 ) * stitchesperinch - underarmcastoncount

function calcFrontandbackstitchcountchest ( thechestcircumferenceinches, thestitchesperinch, theunderarmcastoncount  ){
	theCalculation = ( thechestcircumferenceinches / 2 ) * thestitchesperinch - theunderarmcastoncount
	return theCalculation;

	}


//sleeves stitch count:
//desired sleeve circumference x sts per inch = sleeve st count***
//NOTE: subtract underarmcastoncount from this number to get the number you are increasing to during the raglan shaping
//sleevestitchcountold = sleevecircumferenceinches * stitchesperinch - underarmcastoncount

function calcSleevestitchcount ( thesleevecircumferenceinches , thestitchesperinch ,  theunderarmcastoncount) {
	theCalculation = thesleevecircumferenceinches * thestitchesperinch - theunderarmcastoncount
	return theCalculation;

	}


//Yoke depth
//desired distance from shoulder to underarm x rows/rounds per inch = yoke depth
//yokedepthold = shouldertounderaminches * rowsperinch

function calcYokedepth ( theshouldertounderaminches , therowsperinch ) {
	theCalculation = theshouldertounderaminches * therowsperinch
	return theCalculation;

	}


//desired sleeve lenght: sleeve length x rows per inch
//sleevelengthold = sleevelenghtinches * rowsperinch

function calcSleevelenght ( thesleevelenghtinches , therowsperinch ) {
	theCalculation = thesleevelenghtinches * therowsperinch
	return theCalculation;

	}



var PatternInputClass = {
	stitchesperinch: 0 ,
	rowsperinch: 0 ,
	neckwidthinches: 0 ,
	chestcircumferenceinches: 0 ,
	backtofrontneckdropinches: 0 ,
 	sleevecircumferenceinches: 0 ,
	shouldertounderaminches: 0 ,
	sleevelenghtinches: 0

	};


//  USER INPUT
function getPatternInputFromUser( form ) {

	var patternInput = {};

	patternInput.stitchesperinch = form.stitchesperinch.value;
	patternInput.rowsperinch = form.rowsperinch.value;

	// personal measurements

	patternInput.neckwidthinches = form.neckwidthinches.value;

	patternInput.chestcircumferenceinches = form.chestcircumferenceinches.value;

	patternInput.backtofrontneckdropinches = form.backtofrontneckdropinches.value;

	patternInput.sleevecircumferenceinches = form.sleevecircumferenceinches.value;

	patternInput.shouldertounderaminches = form.shouldertounderaminches.value;

	patternInput.sleevelenghtinches = form.sleevelenghtinches.value;

	return patternInput;



	}
;



var Pattern  = {
	castoncount: 0 ,
	underarmcastoncount: 0 ,
	neckdepth: 0 ,
	frontandbackstitchcountchest: 0 ,
	sleevestitchcount: 0 ,
	yokedepth: 0 ,
	sleevelength: 0

	} ;

// MAIN PART
function calcPattern(patternInput)  {

	pattern = Pattern

	pattern.castoncount = calcCastoncount(patternInput.neckwidthinches, patternInput.stitchesperinch)

	pattern.underarmcastoncount = calcUnderarmcastoncount(patternInput.chestcircumferenceinches, patternInput.stitchesperinch)

	pattern.neckdepth = calcNeckdepth(patternInput.backtofrontneckdropinches, patternInput.rowsperinch)

	pattern.frontandbackstitchcountchest = calcFrontandbackstitchcountchest (patternInput.chestcircumferenceinches, patternInput.stitchesperinch, pattern.underarmcastoncount)

	pattern.sleevestitchcount = calcSleevestitchcount(patternInput.sleevecircumferenceinches, patternInput.stitchesperinch, pattern.underarmcastoncount)

	pattern.yokedepth = calcYokedepth(patternInput.shouldertounderaminches, patternInput.rowsperinch)

	pattern.sleevelength = calcSleevelenght(patternInput.sleevelenghtinches, patternInput.rowsperinch)

	return pattern;

	}


// OUTPUT
function printDebug( pattern )  {

	var note_text = "<br/>You need to cast on " + pattern.castoncount + " stitches.";
	note_text = note_text + "<br/>Your under arm cast on count is " + pattern.underarmcastoncount + " stitches.";
	note_text = note_text + "<br/>You need to increase to " + pattern.frontandbackstitchcountchest + " stitches for front and back.";
	note_text = note_text + "<br/>You need to increase to " + pattern.sleevestitchcount + " sleeve stitches.";
	note_text = note_text + "<br/>You need to knit " + pattern.yokedepth + " rows for your desired yoke depth.";
	note_text = note_text + "<br/>You need to knit " + pattern.sleevelength +  " rows for your desired sleeve length.";


    document.getElementById( "output" ).innerHTML = note_text;
//    document.getElementById( "gauge" ).innerHTML = note_text;

}



function calculatePatternFromHtmlForm( form )  {
	console.trace("hello")
	patternInput = getPatternInputFromUser( form )
	pattern = calcPattern( patternInput )
	printDebug( pattern )

    return false;
}



