from azure.servicebus.control_client import ServiceBusService, Message, Topic, Rule, DEFAULT_RULE_NAME
bus_service = ServiceBusService(
    service_namespace='testingservicebut-001',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='2T7NcAqhNs7Ff3cR6BFCCsiuViccVf76XhuybuhGFRs=')

msg = bus_service.receive_subscription_message('testingtopic', 'GAURAV_RG', peek_lock=False)
print(msg.body)
#print(2)