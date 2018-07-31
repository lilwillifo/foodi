# Foodi

Foodi allows users to track their eating habits and nutrition. Use the search bar to find calorie and nutrition information for any food. When logged in, you can enter the number of servings and save to your daily diary. Save time by selecting from your frequently eaten foods. Then head to the analytics page to see a nutritional breakdown. The deployed version can be found [here](https://foodi-tracker.herokuapp.com/).

## Getting Started

1. Clone this repository.

  ```shell
  git clone git@github.com:lilwillifo/foodi.git
  ```
2. Change into the `foodi` directory

3. Create a virtualenv

  ```shell
  virtualenv -p python3 .venv
  source .venv/bin/activate
  ```
4. Updgrade pip and install dependencies
  ```shell
  pip3 install --upgrade pip
  pip3 install -r requirements/local.txt
  ```

3. Set up the database in psql

  ```shell
  CREATE DATABASE foodi;
  CREATE DATABASE foodi_test;
  ```

4. Migrate and Seed
  ```shell
  python3 manage.py migrate
  python3 manage.py populate_db
  ```

5. Run test suite

  ```shell
    python3 manage.py test
  ```

### Prerequisites

You'll need [Django](https://www.djangoproject.com/) and [Python3](https://www.python.org/downloads/) installed

```
Give examples
```

## Running the tests

Explain how to run the automated tests for this system

## Running the Server Locally

To see your code in action locally, you need to fire up a development server. Use the command:

```shell
python3 manage.py runserver
```

Once the server is running, create an account to start tracking your food.

* `http://localhost:8000/` to run the application.
## Deployment

Deployed project is [here](https://foodi-tracker.herokuapp.com/)

## Contributing

Please follow the Getting Started guide to set up your local dev environment.

This guide assumes that the git remote name of the main repo is `upstream` and that your fork is named `origin`.

Create a new branch on your local machine to make your changes against (based on `upstream/master`):

    git checkout -b branch-name-here --no-track upstream/master

Make sure the tests pass on your new branch:

    `python3 manage.py test`

### Making a change

Make your changes to the codebase. I recommend using TDD. Add a test, make changes and get the test suite back to green.

    `python3 manage.py test`

Once the tests are passing you can commit your changes. See [How to Write a Good Commit Message](https://chris.beams.io/posts/git-commit/) for more tips.

    git add .
    git commit -m "Add a concise commit message describing your change here"

Push your changes to a branch on your fork:

    git push origin branch-name-here
### Submitting a Pull Request

Use the GitHub UI to submit a new pull request against upstream/master. To increase the chances that your pull request is swiftly accepted please have a look at this guide to [making a great pull request](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests)

TL;DR:
* Write tests
* Make sure the whole test suite is passing
* Keep your PR small, with a single focus
* Maintain a clean commit history
* Use a style consistent with the rest of the codebase
* Before submitting, [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) on the current master branch
## Built With

* [Django](https://www.djangoproject.com/) - Web Framework
* [Plotly](https://plot.ly/feed/#/) - Building data visualization
* [Django Rest Framework](http://www.django-rest-framework.org/) - Backend API to feed data to Plotly
* [JQuery](https://jquery.com/) - Asynchronous loading of charts
* [Bootstrap](https://getbootstrap.com/) - Bootstrap for styling


## Authors

* **Margaret Williford**

## Acknowledgments

* A huge shoutout to [Vitor Freitas](https://simpleisbetterthancomplex.com/). For nearly every Django issue I ran into, he had written a blog post to solve my problem.
