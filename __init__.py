from flask import Flask,render_template,request
import pymongo
import homework
import simplejson

app = Flask(__name__)
connection = pymongo.Connection('localhost',27017)
db = connection.db

@app.route('/')
def index():
    return render_template('index.html',hws=homework.hws)

@app.route('/hw/<int:hw_id>/')
def hw(hw_id):
    try:
        # extract the relevant homeworks
        i = [hw.id for hw in homework.hws].index(hw_id)
        hw = homework.hws[i]
        # instantiate questions with seed and parse
        seed = 1
        #questions = [q(seed).parse() for q in hw.questions]
        questions = [q(seed) for q in hw.questions]
        # parse the questions and render HTML
        return render_template('hw.html',name=hw.name, questions=questions)
    except ValueError:
        return '404 Error'

@app.route('/hw/<int:hw_id>/q/<int:q_id>',methods=['GET','POST'])
def question(hw_id,q_id):
    try:
        # extract the relevant homework
        i = [hw.id for hw in homework.hws].index(hw_id)
        hw = homework.hws[i]
        # check the answer
        #return str(request.form.getlist('ans'))
        Q = hw.questions[q_id]
        seed = 1
        q = Q(seed)
        ans = request.form.getlist('ans[]')
        #ans = request.args.getlist('ans[]') # for testing purposes
        return simplejson.dumps(q.check_ans(q.clean(ans)))
    except ValueError:
        return '404 Error'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
