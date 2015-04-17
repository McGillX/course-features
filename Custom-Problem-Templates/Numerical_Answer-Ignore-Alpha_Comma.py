<problem>
<script type="loncapa/python">
import re
import string

def checkAnswer(expect, ans):
	try: 
        #Replace 10 with the correct numerical answer
  		correctAnswer = float(10)
        #Replace 1 with the desired numerical tolerance
  		tolerance = 1
		a1 = str(ans)
        #Removes alpha numerical characters from the answer
		a1Number = re.sub("[A-Za-z]","", a1)
        #Converts commas to decimal points
  		a1Decimal = re.sub(',',".",a1Number)
  		a1Float=float(a1Decimal)
        #Determines how much the students entry deviats from the correct answer
  		toleratedAnswer = abs(correctAnswer-a1Float)
		if tolerance>=toleratedAnswer:
			return True
		else:
			return False
	except ValueError:
		return False
</script>

<p>Question Text</p>
<customresponse cfn="checkAnswer">
        <textline size="40" correct_answer="Correct Answer Displayed to Students" label="Question Text"/><br/>
</customresponse>


    <solution>
        <div class="detailed-solution">
            <p>Explanation</p>
<p> Solution </p>
        </div>
    </solution>
</problem>

