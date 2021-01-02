import dash_core_components as dcc
import dash_html_components as html
import dash


app = dash.Dash()

colors = {'background1': '#FCFCFC', 'background': '#FAFAFA', 'text': '#1b1b1b'}


app.layout = html.Div(children=[
    html.H1('Hello World!', style={'textAlign': 'center', 'color': colors['text']}),
    html.Div('DASH: Welcome to my Dashboard with Python', style={'textAlign': 'center',
                                                                 'color': colors['text']}),


    dcc.Graph(id='example',
              figure = {'data':[
                  {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name': 'SF'},
                  {'x':[1,2,3], 'y':[3,4,7], 'type':'bar', 'name': 'NYC'}],


                    'layout':{
                        'plot_bgcolor':colors['background'],
                        'paper_bgcolor':colors['background'],
                        'font': {'color':colors['text']},
                        'title':'BAR PLOTS!'

                    }})
], style={'backgroundColor': colors['background1']}

)



if __name__ == '__main__':
    app.run_server()
