# AWS Step Functions

> AWS Step Functions is a fully managed and serverless orchestration service from AWS that allows us to coordinate and orchestrate multiple AWS services

![img](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfx0TCxHiL6qajOxQ5b0FatEc-rqavugS-M4xqbRqfBFQLG5F6fzBgYgbYSVJA7b-FKhw7eQ2hWA2WeZpAXsmVNEplYMqMkHl_5rFdb1V7GJU5VUHl6KwSR1bZ5UEluxbEjw13OXf2v5pKhZbV5-FYALf8XrHw=s2048?key=9LGygfnpIRoi04z45gT3Xw)

**Key Components**

1. State Machine : A state machine defines the workflow in Step Functions.
2. States : States represents individual actions or decisions within the workflow.
3. Transitions : Transition define how the execution moves from one state to another.
4. Input / Output : Each state can receive input from the previous state of external service (JSON), States can producer output that can be used as input to others statse 



**States**

1. Task State
2. Choice State
3. Wait State
4. Succeed State
5. Fail State
6. Parallel State

 

```
{
    "StartAt": "ProcessFile",
    "States": {
        "ProcessFileState": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:region:account-id:function:ProcessFileFunction",
            "Next": "BranchBasedOnXTransitionState"
        },
        "BranchBasedOnXTransitionState": {
            "Type": "ChoiceTask",
            "Choices": [{
                    "Variable": "$.x",
                    "NumericLessThan": 5,
                    "Next": "HandleXLessThan5TransitionState"
                }
        }
    }
}

```

