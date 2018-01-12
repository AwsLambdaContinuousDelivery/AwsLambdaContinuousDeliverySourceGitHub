#!/usr/bin/env python

from distutils.core import setup

setup( name='AwsLambdaContinuousDeliverySourceGitHub'
     , version = '0.0.1'
     , description = 'AwsLambdaContinuousDeliverySourceGitHub'
     , author = 'Janos Potecki'
     , url = 'https://github.com/AwsLambdaContinuousDelivery/AwsLambdaContinuousDeliverySourceGitHub'
     , packages = ['awslambdacontinuousdelivery.source.github']
     , license='MIT'
     , install_requires = [ 
          'troposphere'
        ]
     )
