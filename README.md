# Chuck Norris Jokes and Currency Exchange Project
This project was developed as a university assignment that demonstrates the usage of APIs. The project incorporates two APIs: one for retrieving jokes about Chuck Norris and another for currency exchange rates.

## Chuck Norris Jokes API
The Chuck Norris Jokes API is used to fetch random jokes about Chuck Norris. The jokes are displayed as Windows notifications. Here's how it works:

   1) A GET request is made to the Chuck Norris Jokes API to retrieve a random joke.
   2) The obtained joke is saved in a JSON file named "chuck_norris.json".
   3) The joke is printed to the console.
   4) A Windows notification is displayed, showing the joke.
## Currency Exchange API
   1) The user is prompted to input the three-letter codes for the currency they want to exchange from  and the currency they want to exchange to.
   2) The user is also prompted to input the amount of money they want to exchange 
   3) A GET request is made to the Exchange Rate API  using the provided API key, currency codes, and pair information.
   4) The response status code, text, content, and headers are printed to the console.
   5) The response is parsed as JSON, and the resulting data is saved in a JSON file named "currency.json".
   6) The exchange rate and conversion result are printed to the console.
## SQLite Database
The project utilizes an SQLite database to store the important information obtained from the APIs. Here's how it works:

   1) A connection is established with an SQLite database named "api.sqlite".
   2) If the "api_infos" table doesn't exist, it is created with columns for ID (auto-incremented), title, main, rate, and total.
   3) The important information from both APIs, such as jokes and currency exchange rates, is inserted into the "api_infos" table.
   4) The changes are committed to the database, and the connection is closed.



Please note that the project requires the installation of the following libraries: win10toast, requests, json, and sqlite3. Additionally, it's important to handle any potential exceptions or errors that may occur during the execution of the code.
