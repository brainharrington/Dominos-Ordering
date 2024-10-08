This is part two of working on ordering groceries through a custom gpt. First we learned how to deploy a public api endpoint and then we learned how to add talking to that endpoint as an action in a custom gpt.

That project was for calling one random cat fact.

Now we're moving on to ordering a pizza from the dominos api. We are using the main exisitng python wrapper of the popular node.js project for ordering the dominos pizza.

The first approach we want to take is just listing the python wrapper as a dependency and creating the api endpoint like we did with the cat fact project.

Last time we got stuck on error codes for the items on the menu because we were not able to successfully retrieve the menu.

So goal is to get past that and create an endpoint and then use a custom gpt to order pizza through the endpoint.