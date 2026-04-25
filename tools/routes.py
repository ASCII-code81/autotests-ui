from enum import Enum


class AppRoute(str, Enum):
    LOGIN = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    REGISTRATION = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

    DASHBOARD = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"

    COURSES = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    COURSES_CREATE = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"