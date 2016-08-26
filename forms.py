from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired

class AddTaskForm(Form):
    task_id=IntegerField()
    name=StringField('Tarefa', validators=[DataRequired()])
    due_date=DateField(
        'Limite (dd/mm/yyyy)',
        validators=[DataRequired()],format='%d/%m/%Y'
        )
    priority=SelectField(
        'Prioridade',
        validators=[DataRequired()],
        choices=[
            ('1','Emergente'),('2','Urgente'),('3','Tranquilo')
            ]
    )
    status=IntegerField('Status')
    user=SelectField(
        'Para',
        validators=[DataRequired()],
        choices=[
            ('nuno','Nuno'),('jojo','Jojo'),('Ambos','both')
        ]
    )
        