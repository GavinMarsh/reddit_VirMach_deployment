#!/usr/bin/env python3

from flask import Flask

def create_app(config):
    # create app and load config
    app = Flask(__name__)
    app.config.from_object(config)

    # initalize app with database
    from model import db
    db.init_app(app)

    # bind views
    from view import index, all_dates, by_date, all_subreddits, by_subreddit
    app.add_url_rule('reddit/', view_func=index)
    app.add_url_rule('reddit/date', view_func=all_dates)
    app.add_url_rule("reddit/date/<day_to_pull>", view_func=by_date)
    app.add_url_rule('reddit/sub', view_func=all_subreddits)
    app.add_url_rule('reddit/sub/<sub_to_pull>', view_func=by_subreddit)

    return app
