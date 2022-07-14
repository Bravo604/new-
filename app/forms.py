from flask_wtf import FlaskForm
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=8, max=64)
    ])
    submit = wf.SubmitField('OK')

    def validate(self):
        if not super().validate():
            return False
        # needed_symbols = '!@#$%'
        # for i in needed_symbols:
        #     if i not in self.password.data:
        #         self.password.errors.append('Пароль должен содержать символы  !@#$%')
        #         return False

        if self.password.data.isdigit():
            self.password.errors.append('Пароль не может состоять только из цифр')
            return False

        if self.password.data.isalpha():
            self.password.errors.append('Пароль не может состоять только из букв')
            return False

        return True


class PostForm(FlaskForm):
    title = wf.StringField('Заголовок', validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField('Текст новости', validators=[wf.validators.DataRequired()])
    is_boom_news = wf.BooleanField('Супер новость')
    submit = wf.SubmitField('OK')
