# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:00:09 2019

@author: Rajkumar Shinde
"""

#import unittest
#from newsapi_cli.sqlclient import SqlClient


from unittest import TestCase
from newsapi_cli.news import news

class TestConsole(TestCase):
    def test_basic(self):
        news.main('test_out.csv')





#from click.testing import CliRunner
#from newsapi_cli import news
#
#
#def test_news_cli_success():
#    runner = CliRunner()
#    result = runner.invoke(news, ['test_out.csv'])
#    assert result.exit_code == 0
#    assert result.output == ''
#    assert result.exception is None


#def test_cli_hello_fail():
#    runner = CliRunner()
#    result = runner.invoke(cli, ['hello'])  # Forget to pass a "name" argument
#    assert result.exit_code == 2
#    assert 'Usage: cli hello' in result.output
#    assert 'Error: Missing argument "name".' in result.output
#    assert isinstance(result.exception, SystemExit)
#
#
#def test_cli_hello_help():
#    runner = CliRunner()
#    result = runner.invoke(cli, ['hello', '--help'])
#    assert result.exit_code == 0
#    assert 'Usage: cli hello [OPTIONS] NAME' in result.output
#    assert result.exception is None