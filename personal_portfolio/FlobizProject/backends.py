#!/usr/bin/python
# -*- coding: utf-8 -*-
from FlobizProject.models import Users
import logging


class MyAuthBackend(object):

    def authenticate(self, email, password):
        try:
            user = Users.objects.get(email=email)
            print ('return none', user)
            if user.check_password(password):
                return user
            else:
                return None
        except Users.DoesNotExist:
            logging.getLogger('error_logger'
                              ).error('user with login %s does not exists '
                     % login)
            return None
        except Exception as e:
            logging.getLogger('error_logger').error(repr(e))
            print('exception', e)
            return None

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            print('exception user not found')
            logging.getLogger('error_logger'
                              ).error('user with %(user_id)d not found')
            return None
