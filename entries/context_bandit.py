from recogym.agents import LogregMulticlassIpsAgent, logreg_multiclass_ips_args
logreg_multiclass_ips_args['num_products'] = P

agent = build_agent_init('Contextual Bandit', LogregMulticlassIpsAgent, {**logreg_multiclass_ips_args,})
