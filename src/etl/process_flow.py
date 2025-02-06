import pandas as pd
from sqlalchemy import create_engine
from utils import load_db_config
import pm4py
from pm4py.objects.log.obj import EventLog
from pm4py.objects.log.util import dataframe_utils
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer



def load_event_log():
    db_config = load_db_config()
    db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
    engine = create_engine(db_url)

    query = 'SELECT * FROM event_logs ORDER BY case_id, event_timestamp'
    df = pd.read_sql(query, con=engine)
    return df


# Convert event_log for pm4py
def process_mining_analysis():
    df = load_event_log()

    df.rename(columns={'case_id': "case:concept:name", "event_name":"concept:name", "event_timestamp":"time:timestamp"}, inplace=True)

    df['time:timestamp'] = pd.to_datetime(df['time:timestamp'])

    # Convert to event_log format
    event_log = pm4py.format_dataframe(df, case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')

    # Generate process model vizualization
    dfg, start_activities, end_activities = pm4py.discover_directly_follows_graph(event_log)
    # pm4py.view_dfg(dfg, start_activities, end_activities)
    print("DONE")
    #Most Common Process Flow
    # pm4py.discover_heuristics_net(event_log)
    
    # Average time between events
    # pm4py.stats.get_trace_attribute_values(event_log, 'case:atribute', case_id_key=)

    # net, initial_marking, final_marking = alpha_miner.apply(event_log) 
    # gviz = pn_visualizer.apply(net, initial_marking, final_marking)
    # pn_visualizer.view(gviz) 

    bpmn_model = pm4py.discover_bpmn_inductive(event_log)
    pm4py.view_bpmn(bpmn_model)


if __name__ == "__main__":
    process_mining_analysis()