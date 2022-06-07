# ... Cheat Sheet/Notes <a id ='top'></a>

<br>
<br>

# Contents

- [Job: Deploy CFN Infra](#1)
- [Command : Destroy CFN Infra on Fail](#2)
- [Jobs Add keyPair Fingerprint](#3)
- [Jobs: Smoke test](#4)
- [Workflows: Syntax Example](#5)
- [](#6)
- [](#7)
- [](#8)
- [](#9)
- [](#10)
- [](#11)
- [](#12)
- [](#13)
- [](#14)
- [](#15)
- [](#16)
- [](#17)
- [](#18)
- [](#19)
- [](#20)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [go to top](#top)

<br>
<br>
<br>

# Job: Deploy CFN Infra <a id='1'></a> ([go to top](#top))

```yml
version 2.1

jobs:
  createInfra:
    docker:
      - image: amazon/aws-cli
    steps:
      - checkout
      - run:
          name: Create Cloudformation Stack
          command: |
            aws cloudformation deploy \
            --template-file template.yml \
            --stack-name myStack-${CIRCLE_WORKFLOW_ID:0:5} \
            --region us-east-1
```

```yml
jobs:
  create_infrastructure:
    docker:
      - image: amazon/aws-cli
    steps:
      - checkout
      - run:
          name: Create Cloudformation Stack
          command: |
            aws cloudformation deploy \
              --template-file template.yml \
              --stack-name myStack-${CIRCLE_WORKFLOW_ID:0:5} \
              --region us-east-1
      # Fail the job intentionally to simulate an error.
      # Uncomment the line below if you want to fail the current step
      # - run: return 1
      - destroy_environment
```

```yml
jobs:
  create_and_deploy_front_end:
    docker:
      - image: amazon/aws-cli
    steps:
      - checkout
      - run:
          name: Execute bucket.yml - Create Cloudformation Stack
          command: |
            aws cloudformation deploy \
            --template-file bucket.yml \
            --stack-name stack-create-bucket-${CIRCLE_WORKFLOW_ID:0:7} \
            --parameter-overrides MyBucketName="mybucket-${CIRCLE_WORKFLOW_ID:0:7}"
      # upload all contents of the current directory to the S3 bucket
      - run: aws s3 sync . s3://mybucket-${CIRCLE_WORKFLOW_ID:0:7} --delete
```

<br>
<br>
<br>

# Command : Destroy CFN Infra on Fail <a id='2'></a> ([go to top](#top))

```yml
commands:
  destroy_environment:
    steps:
      - run:
          name: Destroy environment
          when: on_fail
          command: |
            aws cloudformation delete-stack --stack-name myStack-${CIRCLE_WORKFLOW_ID:0:5}
```

<br>
<br>
<br>

# Jobs Add keyPair Fingerprint <a id='3'></a> ([go to top](#top))

```yml
jobs:
  configure_infrastructure:
    docker:
      - image: python:3.7-alpine3.11
    steps:
      - checkout
      - add_ssh_keys:
          fingerprints: ["38:06:14:b1:78:21:44:1d:72:fd:2b:83:69:43:ab:c8"]
      - run:
          name: Install ansible
          command: |
            # install the dependencies needed for your playbook
            apk add --update ansible
      - run:
          name: Configure server
          command: |
            ansible-playbook -i inventory.txt main4.yml
```

<br>
<br>
<br>

# Jobs: Smoke test <a id='4'></a> ([go to top](#top))

```yml
jobs:
  smoke_test:
    docker:
      - image: alpine:latest
    steps:
      - run: apk add --update curl
      - run:
          name: smoke test
          command: |
            URL="https://blog.udacity.com/"
            # Test if website exists
            if curl -s --head ${URL} 
            then
              return 0
            else
              return 1
            fi
      - destroy_environment
```

<br>
<br>
<br>

# Workflows: Syntax Example <a id='5'></a> ([go to top](#top))

```yml
workflows:
  default:
    jobs:
      - build-frontend
      - build-backend
      - test-frontend:
          requires: [build-frontend]
      - test-backend:
          requires: [build-backend]
      - scan-backend:
          requires: [build-backend]
      - scan-frontend:
          requires: [build-frontend]
      - deploy-infrastructure:
          requires: [test-frontend, test-backend, scan-frontend, scan-backend]
          filters:
            branches:
              only: [test-feature-branch]
      - configure-infrastructure:
          requires: [deploy-infrastructure]
      - run-migrations:
          requires: [configure-infrastructure]
      - deploy-frontend:
          requires: [run-migrations]
      - deploy-backend:
          requires: [run-migrations]
      - smoke-test:
          requires: [deploy-backend, deploy-frontend]
      - cloudfront-update:
          requires: [smoke-test]
      - cleanup:
          requires: [cloudfront-update]
```

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>

# Title <a id=''></a> ([go to top](#top))

<br>
<br>
<br>
