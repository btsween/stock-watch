## About

The purpose of this application is to create an automated bot that looks for irrational pricing in the market. Specifically, the program searches for stocks that are priced low compared to both historic averages and recent averages, which might indicate that it is oversold due to some recent news. Upon discovering these pricing situations, the application sends a text message to the user through Twilio to create an alert system.

## Environment Setup

This application requires a Twilio account in order to deliver SMS communication.

1.  Reference `.env.example` for the neccesary Twilio account information
2.  Load these variables as to process env
3.  `pip install twilio`
4.  `python app.py`

## Future Work

There is a backlog of features to implemented on this application.

- Test suite
- Deploy with database of users to send alerts to
- Additional pricing models
