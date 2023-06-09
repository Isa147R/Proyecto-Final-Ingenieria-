import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from Connection1 import Connection1
import ProyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


# ------------------------------------------------- Graficos Barras -------------------------------------------------

# Usuarios por zona
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_zona(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["zona","personas_utilizan_transporte"])
figBarCases = px.bar(dfCases.head(20),x="zona", y="personas_utilizan_transporte",color_discrete_sequence=['#dde5b6'])

# Configurar la fuente en los gráficos Usuarios por zona
figBarCases.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# Usuarios por estacion
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.usuarios_por_estacion(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["estacion","personas_utilizan_transporte"])
figBarCases1 = px.bar(dfCases.head(20),x="estacion", y="personas_utilizan_transporte",color_discrete_sequence=['#dde5b6'])

# Configurar la fuente de los graficos Usuarios por estacion
figBarCases1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)


# Usuarios por tipo_perfil
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.tipo_perfil_mas_utilizado(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["perfil","total_utilizado"])
figBarCases2 = px.bar(dfCases.head(20),x="perfil", y="total_utilizado",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Usuarios por tipo de perfil 
figBarCases2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# salidas por estaciones
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_por_estacion(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["nombre","total_salidas"])
figBarCases3 = px.bar(dfCases.head(20),x="nombre", y="total_salidas",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)



# ------------------------------------------------- Graficos pie -------------------------------------------------

#--zonas
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.generar_grafico_pie_zonas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","zona"])
figPie1 = px.pie(dfCases, values='cantidad', names='zona', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie1.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.generar_grafico_pie_zonas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","zona"])
figBarCases4 = px.bar(dfCases.head(20),x="cantidad", y="zona",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases4.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

# --------AMERICAS

con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_americas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie2 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_americas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases5 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases5.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---NQSUR
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NQSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie3 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie3.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NQSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases6 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases6.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---CALLE80
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE80(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie4 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie4.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE80(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases7 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases7.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---CALLE26
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE26(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie5 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie5.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CALLE26(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases8 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases8.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---CARACAS
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACAS(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie6 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie6.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACAS(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases9 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases9.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---carrera10
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARRERA10(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie7 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie7.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARRERA10(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases10 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases10.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---suba
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_SUBA(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie8 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie8.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_SUBA(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases11 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases11.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---caracassur
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACASSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie9 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie9.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_CARACASSUR(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases12 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases12.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)

#---norte
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NORTE(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figPie10 = px.pie(dfCases, values='cantidad', names='estacion', color_discrete_sequence=['#bc6c25'])

# Configurar la fuente de los gráficos Salidas por zonas
figPie10.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#FDFFFC',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.salidas_NORTE(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["cantidad","estacion"])
figBarCases13 = px.bar(dfCases.head(20),x="cantidad", y="estacion",color_discrete_sequence=['#dde5b6'])

#Configurar la fuente de los graficos Salidas por estaciones
figBarCases13.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
# ------------------------------------------------- Analisis Hora-------------------------------------------------
#--americas
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_americas(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases14 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases14.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab12_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Americas"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases14,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--bosa
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_bosa(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases15 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases15.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab13_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Bosa"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases15,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--80
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_80(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases16 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases16.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab14_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora CALLE 80"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases16,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--bolivar
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_bolivar(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases17 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases17.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab15_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Bolivar"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases17,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--engativa
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_engativa(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases18 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases18.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab16_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Engativa"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases18,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--fontibon
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_fontibon(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases19 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases19.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab17_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Fontibon"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases19,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--kennedy
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_kennedy(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases20 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases20.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab18_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Kennedy"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases20,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--perdomo
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_perdomo(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases21 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases21.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab19_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Perdomo"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases21,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})

#--cristobal
con = Connection1()
con.openConnection1()
query = pd.read_sql_query(sql.hora_cristobal(),con.connection)
con.closeConnection1()
dfCases = pd.DataFrame(query,columns=["hora_del_dia","cantidad_transacciones"])
figBarCases22 = px.bar(dfCases.head(20),x="hora_del_dia", y="cantidad_transacciones",color_discrete_sequence=['#dde5b6'])
figBarCases22.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='#283618',
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="#FFFFFC"
    )
)
tab20_content = dbc.Card([
    dbc.CardBody([
        html.H3("Registros por hora Cristobal"),
        dcc.Graph(
            id='piechart',
            figure=figBarCases22,
            style={'width': '100%'}
        )
    ]),    
], className="mt-4", style={'background-color': '#283618'})
# ------------------------------------------------- Tabs Graficos de Pie -------------------------------------------------
tab2_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros por Linea"),
        dcc.Graph(
            id='piechart',
            figure=figPie1,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases4,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab3_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Americas"),
        dcc.Graph(
            id='piechart',
            figure=figPie2,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases5,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab4_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros NQS Sur"),
        dcc.Graph(
            id='piechart',
            figure=figPie3,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases6,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab5_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Calle 80"),
        dcc.Graph(
            id='piechart',
            figure=figPie4,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases7,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab6_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Calle 26"),
        dcc.Graph(
            id='piechart',
            figure=figPie5,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases8,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab7_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Caracas"),
        dcc.Graph(
            id='piechart',
            figure=figPie6,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases9,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab8_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Carrera 10"),
        dcc.Graph(
            id='piechart',
            figure=figPie7,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases10,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab9_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Suba"),
        dcc.Graph(
            id='piechart',
            figure=figPie8,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases11,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})

tab10_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Caracas Sur"),
        dcc.Graph(
            id='piechart',
            figure=figPie9,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases12,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})


tab11_content = dbc.Card([
    dbc.CardBody([
        html.H3("Cantidad de registros Norte"),
        dcc.Graph(
            id='piechart',
            figure=figPie10,
            style={'width': '100%'}
        ),
        dcc.Graph(
            id='piechart',
            figure=figBarCases13,
            style={'width': '100%'}
        )
    ]),
    
], className="mt-4", style={'background-color': '#283618'})



# ------------------------------------------------- Layout-------------------------------------------------

app.layout = html.Div(children=[
    # ------------------------------------------------- Encabezado -------------------------------------------------
    html.H1(children='Analisis Sistema de Transporte Masivo Bogota', style={'margin-left': '35px'}),
    html.H6(children='Isabela Ruiz', style={'margin-left': '35px'}),
    html.Div(style={'height': '50px'}),
    # ------------------------------------------------- Tabs Pie-------------------------------------------------
    dbc.Tabs([
        dbc.Tab(tab2_content, label="Analisis por Linea"),
        dbc.Tab(tab3_content, label="Linea Americas"),
        dbc.Tab(tab4_content, label="Linea  NQS Sur"),
        dbc.Tab(tab5_content, label="Linea Calle 80"),
        dbc.Tab(tab6_content, label="Linea  Calle 26"),
        dbc.Tab(tab7_content, label="Linea  Caracas"),
        dbc.Tab(tab8_content, label="Linea  Carrera 10"),
        dbc.Tab(tab9_content, label="Linea  Suba"),
        dbc.Tab(tab10_content, label="Linea  Caracas Sur"),
        dbc.Tab(tab11_content, label="Linea  Norte"),
    ]),
    # ------------------------------------------------- Graficos de barras -------------------------------------------------
    # Usuarios por zona
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Usuarios por zona", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barusuarios_por_zona',
                            figure=figBarCases,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cuántas personas utilizan el transporte público en una zona en particular? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT z.nombre AS zona, SUM(s.total) AS personas_utilizan_transporte
                        FROM Salidas s
                        JOIN Estacion e ON s.id_Estacion = e.id
                        JOIN Linea l ON e.id_Linea = l.id
                        JOIN Zona z ON l.id_Zona = z.id
                        JOIN Mes m ON s.id_Mes = m.id
                        WHERE m.id = 1
                        GROUP BY zona
                        ORDER BY personas_utilizan_transporte DESC;"""),                        
                    ]
                )
            ]
        ),
    # Usuarios por estacion                            
    html.Div(style={'height': '50px'}),                            
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Usuarios por estacion", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barusuarios_por_estacion',
                            figure=figBarCases1,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cuántas personas utilizan el transporte público por estacion? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT e.nombre AS estacion, SUM(s.total) AS personas_utilizan_transporte
                        FROM Salidas s
                        JOIN Estacion e ON s.id_Estacion = e.id
                        JOIN Mes m ON s.id_Mes = m.id
                        WHERE m.id = 1
                        GROUP BY e.nombre
                        ORDER BY personas_utilizan_transporte DESC; """),                        
                    ]
                )
            ]
        ),
    # Usuarios por perfil                            
    html.Div(style={'height': '50px'}),
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Perfil mas utilizado", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='bartipo_perfil_mas_utilizado',
                            figure=figBarCases2,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Cual es el perfil de tarjeta mas utilizado? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT tp.nombre AS perfil, COUNT(*) AS total_utilizado
                        FROM Tarjeta t
                        JOIN Tipo_perfil tp ON t.id_Tipo_perfil = tp.id
                        GROUP BY tp.nombre
                        ORDER BY total_utilizado DESC; """),                        
                    ]
                )
            ]
        ),
    # Salidas por estacion                            
    html.Div(style={'height': '50px'}),
    html.Div(
            className='container',
            style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px','font-family': 'Arial, sans-serif'},
            children=[
                html.Div(
                    style={'width': '50%'},
                    children=[
                        html.Div(style={'height': '30px'}),
                        html.Div(
                            style={'width': '50%', 'display': 'flex', 'justify-content': 'flex-end', 'margin-left': '0px'},
                            children = [
                                html.H3("Salidas por estacion", style={'margin-left': '50px'})
                            ]
                            ),  
                        dcc.Graph(
                            id='barsalidas_por_estacion',
                            figure=figBarCases3,
                            style={'width': '100%'}
                        )
                    ]
                ),
                html.Div(
                    style={'margin-left': '20px', 'width': '50%', 'white-space': 'pre-wrap'},
                    children=[
                        html.H3(" ¿Ques estaciones registraron mas salidas? "),
                        html.Div(style={'height': '20px'}),
                        html.H6("""
                        SELECT Estacion.nombre, SUM(Salidas.total) AS total_salidas
                        FROM Salidas
                        JOIN Estacion ON Salidas.id_Estacion = Estacion.id
                        JOIN Mes ON Salidas.id_Mes = Mes.id
                        WHERE Mes.id=1
                        GROUP BY Estacion.nombre
                        ORDER BY total_salidas DESC
                        LIMIT 5; """),                        
                    ]
                )
            ]
        ),
   dbc.Tabs([
       dbc.Tab(tab12_content, label="Horas Americas"),
       dbc.Tab(tab13_content, label="Horas Bosa"),
       dbc.Tab(tab14_content, label="Horas Calle 80"),
       dbc.Tab(tab15_content, label="Horas Bolivar"),
       dbc.Tab(tab16_content, label="Horas Engativa"),
       dbc.Tab(tab17_content, label="Horas Fontibon"),
       dbc.Tab(tab18_content, label="Horas Kennedy"),
       dbc.Tab(tab19_content, label="Horas Perdomo"),
       dbc.Tab(tab20_content, label="Horas Cristobal"),
   ]),
    # ------------------------------------------------- Tabs Grafico Lineas -------------------------------------------------                            
    
    html.Label('Color Picker'),
    dcc.Input(
        id='our-color-picker',
        type='text',
        value='#119DFF',
        style={'width': '80px'}
    ),

], style={'background': '#606c38', 'color': '#FFFFFC',})




if __name__ == '__main__':
    app.run_server(debug = True)
    
    
