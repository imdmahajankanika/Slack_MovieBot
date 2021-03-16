# Slack_MovieBot
<ul>
	<li> This is a chatbot created using <b>Slack</b> platform and <b>IBM Watson Assistant</b> for NLP processing.</li>
	<li> It uses a recommendation system (<b>metadata based collaborative filtering</b>) to suggest <b>similar movies</b> with their IMDB links and posters.</li>
	<li> It also addresses below queries:-
		<ul>
			<li> <b>Movie Overview</b> </li>
			<li> <b>Movie Genre</b> </li>
			<li> <b>Budget</b> </li>
			<li> <b>Revenue</b> </li>
			<li> <b>Ratings</b> </li>
			<li> <b>No. of votes/Voter Count</b> </li>
			<li> <b>IMDB Link</b> </li>
			<li> <b>TMDB Link</b> </li>
			<li> <b>Check for adult content</b> </li>
			<li> <b>Recommendation for similar movies</b> </li>
		</ul>
	</li>
</ul>

## MovieBot setup prerequisites:-
<ul>
	<li> Install the required python libraries (used Python 3.9.0 in this case)
		<ul>
			<li>pandas==1.1.4</li>
			<li>slackclient==1.2.1</li>
			<li>watson-developer-cloud>=2.4.0</li>
			<li>nltk==3.5</li>
			<li>sklearn==0.23.2</li>
			<li>joblib==0.17.0</li>
		</ul>
	<li>Create a Slack classic app <a href="https://api.slack.com/apps?new_classic_app=1">click here</a>  and install it to your Slack workspace. </li>
	<li>Make a note of <b>"Verification Token"<b> and <b>"Bot User OAuth Token".</b></li>
	<li>Setup IBM Watson Assitant <a href="https://cloud.ibm.com/docs/assistant-data?topic=assistant-data-getting-started"> Click here </a>, create a dialog skill and add intent and entites.</li>
	<li>Make a note of <b>"Assistant API Key"<b> and <b>"Assistant skill Id".</b></li>		
	<li>Integrate Watson Assistant with Slack <a href="https://cloud.ibm.com/docs/assistant?topic=assistant-deploy-slack"> Click here</a></li>
	
</ul>

## How to initiate MovieBot...
<ul>
	<li> Clone this project and update config files for <b>"Verification Token"<b>, <b>"Bot User OAuth Token"</b>, <b>"Assistant API Key"<b> and <b>"Assistant skill Id".</li>
	<li> Execute <b>collabFilter.py<b> present under nlp/recommendation_Sys so as to generate a .joblib file storing the variables, matrices to be used for recommendation system.</li>
	<li> Run main.py and you will get a message <b>'MovieBot connected and running!'<b> on successful connection.
</ul>

## How to use...
<img src="">
<img src="">
<img src="">



