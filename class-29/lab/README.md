# Lab: Django Custom User

## Overview

Django does a great job at allowing to get started with a solid foundation. But a foundation is just the beginning. We still need to "build the house."

One of the first things many developers choose to do is to create a custom user model.

## Feature Tasks and Requirements

- create Django application `django-custom-user` from scratch that has a custom user model named `CustomUser`
- Custom user should use *email* instead of *username* for signup / login
- Application should work with Django Admin
- Use the very helpful [tutorial](https://learndjango.com/tutorials/django-custom-user-model){:target="_blank"} at [LearnDjango](https://learndjango.com/){:target="_blank"}

## Implementation Notes

- Make sure to create custom user model **before** migrating data
- **WARNING** Django version 5 no longer supports logging out with a GET request.
  - Refer to demo for safe logging out in Django 5.

### User Acceptance Tests

- Verify the creation of a new user with email and password
- Verify that duplicate emails are not allowed

## Configuration

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

## Stretch

- Create a Django application using [DjangoX](https://github.com/wsvincent/djangox){:target="_blank"}
- Style form using [Django Widget Tweaks](https://prettyprinted.com/tutorials/django-widget-tweaks/){:target="_blank"}
