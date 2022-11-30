from env_contraints import stream_name, client

shard = client.get_shard_iterator(
    StreamName = stream_name,
    ShardId = 'shardId-000000000002',
    ShardIteratorType = 'LATEST'
    )['ShardIterator']
    
while shard is not None:
    #choose which shard will be get
    results = client.get_records(ShardIterator = shard)
    records = results['Records']
    #prevents to get the same data multiple times
    shard = results['NextShardIterator']
    
    for record in records:
        #prevents bad characters in some languages due unicode  
        print(str(record['Data'].decode('unicode-escape')))
        