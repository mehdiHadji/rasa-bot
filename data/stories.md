## certif path 1
* greet
  - utter_greet
* demand_certif
  - action_demand_certif
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## certif path 2
* demand_certif
  - action_demand_certif
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## certif path 3
* greet
  - utter_greet
* demand_certif
  - action_demand_certif
  - utter_did_that_help
* deny
  - utter_ask_again
* demand_certif
  - action_demand_certif
  - utter_did_that_help
* affirm or thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## greet path
* greet
  - utter_greet

## goodbye path
* goodbye
  - utter_goodbye

## fallback
- utter_unclear
