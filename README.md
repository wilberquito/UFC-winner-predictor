# ufc

I'll try to predict winners next clash

<details>

<summary>Data information</summary>

    "\n",
    "| **Variable**                                                    | **Description**                                                     |\n",
    "|-----------------------------------------------------------------|---------------------------------------------------------------------|\n",
    "| R_fighter                                                       | favorite fighter in match up                                        |\n",
    "| B_fighter                                                       | underdog fighter in match up                                        |\n",
    "| date                                                            | when the fight took place                                           |\n",
    "| location                                                        | city where the fight took place                                     |\n",
    "| country                                                         | country where the fight took place                                  |\n",
    "| winner                                                          | which fighter won the fight                                         |\n",
    "| weight_class                                                    | weight class where the fight took place in                          |\n",
    "| gender                                                          | gender of the fighters                                              |\n",
    "| R/B_Stance                                                      | fight stance of the underdog/favorite fighter                       |\n",
    "| finish                                                          | how did the fight end                                               |\n",
    "| finish_details                                                  | specifically how did the fight end                                  |\n",
    "| finish_round_time                                               | time in the round when the fight ended                              |\n",
    "| title_bout                                                      | was the fight a title bout                                          |\n",
    "| R/B_odds                                                        | betting odds of the favorite/underdog                               |\n",
    "| R/B_ev                                                          | payout for favorite/underdog win                                    |\n",
    "| no_of_rounds                                                    | number of rounds for the fight                                      |\n",
    "| R/B_current_lose_streak                                         | number of consecutive losses at time of fight                       |\n",
    "| R/B_current_win_streak                                          | number of consecutive wins at time of fight                         |\n",
    "| R/B_draw                                                        | total number of draw up until time of fight                         |\n",
    "| R/B_losses                                                      | total number of losses up until time of fight                       |\n",
    "| R/B_wins                                                        | total number of wins up until time of fight                         |\n",
    "| R/B_longest_win_streak                                          | longest win streak in career up until time of fight                 |\n",
    "| R/B_avg_SIG_STR_landed                                          | average number of significant strikes landed per minute             |\n",
    "| R/B_avg_SIG_STR_pct                                             | accuracy of significant strikes landed vs thrown                    |\n",
    "| R/B_avg_SUB_ATT                                                 | average number of submission attempts in a fight                    |\n",
    "| R/B_avg_TD_landed                                               | average number of takedowns landed per minute                       |\n",
    "| R/B_avg_TD_pct                                                  | accuracy of takedown landed vs attempted                            |\n",
    "| R/B_Height_cms                                                  | height of respective fighter in match up                            |\n",
    "| R/B_Reach_cms                                                   | reach of respective fighter in match up                             |\n",
    "| R/B_weight_lbs                                                  | weight of respective fighter in match up                            |\n",
    "| R/B_age                                                         | age of respective fighter in match up                               |\n",
    "| R/B_total_title_bouts                                           | total number of in career up until the time of fight                |\n",
    "| R/B_total_round_fought                                          | total number of rounds fought in the UFC up until fight             |\n",
    "| R/B_win_by_decision                                             | total number of wins respectively by decision                       |\n",
    "| R/B_win_by_submission                                           | total number of wins respectively by submission                     |\n",
    "| R/B_win_by_KO.TKO                                               | total number of wins respectively by knockout                       |\n",
    "| R/B_win_by_TKO_Doctor                                           | total number of wins respectively by doctor stoppage                |\n",
    "| win_dif                                                         | total win differential b/t respective fighter                       |\n",
    "| loss_dif                                                        | total loss differential b/t respective fighter                      |\n",
    "| lose_streak_dif                                                 | losing streak differential b/t respective fighter                   |\n",
    "| win_streak_dif                                                  | win streak differential b/t respective fighter                      |\n",
    "| longest_win_streak_dif                                          | longest win streak differential b/t respective fighter              |\n",
    "| total_round_dif                                                 | differential b/t respective fighter on total rounds fought          |\n",
    "| total_title_bout_dif                                            | differential b/t fighters on total title bouts fought               |\n",
    "| ko_dif                                                          | differential on total knockouts + doctor stoppage wins              |\n",
    "| sub_dif                                                         | differential on total submission wins                               |\n",
    "| sig_str_dif                                                     | differential on significant strikes landed                          |\n",
    "| avg_sub_att_dif                                                 | differential on average submission attempts                         |\n",
    "| avg_td_dif                                                      | differential on takedowns landed                                    |\n",
    "| empty_arena                                                     | was the fight held in an empty arena                                |\n",
    "| R/B_weightclass_rank                                            | weight class rank for respective fighter                            |\n",
    "| finish_round                                                    | which round did the fight end                                       |\n",
    "| total_fight_time_secs                                           | total length of fight in seconds                                    |\n",
    "| R/B_kd_bout                                                     | average number of knockdowns in a bout                              |\n",
    "| R/B_sig_str_landed_bout                                         | average number of significant strikes landed in a bout              |\n",
    "| R/B_sig_str_attempted_bout                                      | average number of significant strikes attempted in a bout           |\n",
    "| R/B_sig_str_pct_bout                                            | average accuracy of significant strikes landed in a bout            |\n",
    "| R/B_tot_str_landed_bout                                         | average total number of strikes landed in a bout                    |\n",
    "| R/B_tot_str_attempted_bout                                      | average total number of strikes attempted in a bout                 |\n",
    "| R/B_td_landed_bout                                              | average number of takedowns landed in a bout                        |\n",
    "| R/B_td_attempted_bout                                           | average number of takedowns attempted in a bout                     |\n",
    "| R/B_td_pct_bout                                                 | average accuracy of takedowns landed in a bout                      |\n",
    "| R/B_sub_attempts_bout                                           | average number of submissions attempted in a bout                   |\n",
    "| R/B_pass_bout                                                   | average number of guard-passes in a bout                            |\n",
    "| R/B_rev_bout                                                    | average number of reversals (i.e., sweeps) in a bout                |"

</details>

## Develop

### Postgres container

```
    cd postgres/ \
    docker build -t postgresdev:latest .
```

```
    docker run -d \
        --name posgresdev \
        -p 5432:5432 \
        -e POSTGRES_PASSWORD=postgres \
        postgresdev:latest
```

You can create a dump with all postgres schema using `pg_dump`

```
    pg_dump -U <user> -W -h localhost ufc > ufc.sql
```

### Mongo container

```
docker run -d --name mongodev \
        -p 27017:27017 \
        -e MONGO_INITDB_ROOT_USERNAME=mongo \
        -e MONGO_INITDB_ROOT_PASSWORD=mongo \
        mongo:latest
```

### DNS resolution

As I don't want to change dns name before run docker compose what I do is

add dns resolution inside '/etc/hosts' file. [source](https://stackoverflow.com/questions/19652555/add-static-dns-entry)

### Run Jupyter in your machine

Create local environment for dependencies

```
    python3 -m venv /path/to/new/virtual/env
```

Install dependencies using pip

```
    pip install -r /path/to/requirements.txt
```

Not you can run jupyter for work

```
    jupyter-lab --ip=0.0.0.0 --no-browser --allow-root
```

## Deliver

The creation of the docker compose is inspired from this [source](https://towardsdatascience.com/dockerizing-jupyter-projects-39aad547484a) 

### Build the project

```
    sudo sh Make.sh
```

### Awake services using docker compose 

```
    docker compose up
```

### Turn off services using docker compose 

```
    docker compose up
```

