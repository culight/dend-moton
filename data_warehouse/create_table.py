2020-10-27 22:53:36.900 DEBUG <ipython-input-11-cfefe9eebbfa> - create_cluster: initializing AWS resources
2020-10-27 22:53:36.910 DEBUG hooks - _alias_event_name: Changing event name from creating-client-class.iot-data to creating-client-class.iot-data-plane
2020-10-27 22:53:36.912 DEBUG hooks - _alias_event_name: Changing event name from before-call.apigateway to before-call.api-gateway
2020-10-27 22:53:36.913 DEBUG hooks - _alias_event_name: Changing event name from request-created.machinelearning.Predict to request-created.machine-learning.Predict
2020-10-27 22:53:36.923 DEBUG hooks - _alias_event_name: Changing event name from before-parameter-build.autoscaling.CreateLaunchConfiguration to before-parameter-build.auto-scaling.CreateLaunchConfiguration
2020-10-27 22:53:36.923 DEBUG hooks - _alias_event_name: Changing event name from before-parameter-build.route53 to before-parameter-build.route-53
2020-10-27 22:53:36.925 DEBUG hooks - _alias_event_name: Changing event name from request-created.cloudsearchdomain.Search to request-created.cloudsearch-domain.Search
2020-10-27 22:53:36.927 DEBUG hooks - _alias_event_name: Changing event name from docs.*.autoscaling.CreateLaunchConfiguration.complete-section to docs.*.auto-scaling.CreateLaunchConfiguration.complete-section
2020-10-27 22:53:36.936 DEBUG hooks - _alias_event_name: Changing event name from before-parameter-build.logs.CreateExportTask to before-parameter-build.cloudwatch-logs.CreateExportTask
2020-10-27 22:53:36.936 DEBUG hooks - _alias_event_name: Changing event name from docs.*.logs.CreateExportTask.complete-section to docs.*.cloudwatch-logs.CreateExportTask.complete-section
2020-10-27 22:53:36.937 DEBUG hooks - _alias_event_name: Changing event name from before-parameter-build.cloudsearchdomain.Search to before-parameter-build.cloudsearch-domain.Search
2020-10-27 22:53:36.937 DEBUG hooks - _alias_event_name: Changing event name from docs.*.cloudsearchdomain.Search.complete-section to docs.*.cloudsearch-domain.Search.complete-section
2020-10-27 22:53:37.039 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/boto3/data/ec2/2016-11-15/resources-1.json
2020-10-27 22:53:37.046 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/endpoints.json
2020-10-27 22:53:37.058 DEBUG hooks - _emit: Event choose-service-name: calling handler <function handle_service_name_alias at 0x10c828170>
2020-10-27 22:53:37.089 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/ec2/2016-11-15/service-2.json
2020-10-27 22:53:37.598 DEBUG hooks - _emit: Event creating-client-class.ec2: calling handler <function add_generate_presigned_url at 0x10c7e5e60>
2020-10-27 22:53:37.661 DEBUG endpoint - create_endpoint: Setting ec2 timeout as (60, 60)
2020-10-27 22:53:37.664 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/_retry.json
2020-10-27 22:53:37.665 DEBUG client - _register_legacy_retries: Registering retry handlers for service: ec2
2020-10-27 22:53:37.667 DEBUG factory - load_from_definition: Loading ec2:ec2
2020-10-27 22:53:37.673 DEBUG hooks - _emit: Event creating-resource-class.ec2.ServiceResource: calling handler <function lazy_call.<locals>._handler at 0x11bc40320>
2020-10-27 22:53:37.676 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/boto3/data/s3/2006-03-01/resources-1.json
2020-10-27 22:53:37.679 DEBUG hooks - _emit: Event choose-service-name: calling handler <function handle_service_name_alias at 0x10c828170>
2020-10-27 22:53:37.684 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/s3/2006-03-01/service-2.json
2020-10-27 22:53:37.701 DEBUG hooks - _emit: Event creating-client-class.s3: calling handler <function add_generate_presigned_post at 0x10c7ea0e0>
2020-10-27 22:53:37.701 DEBUG hooks - _emit: Event creating-client-class.s3: calling handler <function lazy_call.<locals>._handler at 0x11bbe5e60>
2020-10-27 22:53:37.751 DEBUG hooks - _emit: Event creating-client-class.s3: calling handler <function add_generate_presigned_url at 0x10c7e5e60>
2020-10-27 22:53:37.776 DEBUG endpoint - create_endpoint: Setting s3 timeout as (60, 60)
2020-10-27 22:53:37.778 DEBUG client - _register_legacy_retries: Registering retry handlers for service: s3
2020-10-27 22:53:37.780 DEBUG factory - load_from_definition: Loading s3:s3
2020-10-27 22:53:37.782 DEBUG hooks - _emit: Event choose-service-name: calling handler <function handle_service_name_alias at 0x10c828170>
2020-10-27 22:53:37.791 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/iam/2010-05-08/service-2.json
2020-10-27 22:53:37.809 DEBUG hooks - _emit: Event creating-client-class.iam: calling handler <function add_generate_presigned_url at 0x10c7e5e60>
2020-10-27 22:53:37.809 DEBUG regions - _endpoint_for_partition: Using partition endpoint for iam, us-east-2: aws-global
2020-10-27 22:53:37.838 DEBUG endpoint - create_endpoint: Setting iam timeout as (60, 60)
2020-10-27 22:53:37.841 DEBUG client - _register_legacy_retries: Registering retry handlers for service: iam
2020-10-27 22:53:37.843 DEBUG hooks - _emit: Event choose-service-name: calling handler <function handle_service_name_alias at 0x10c828170>
2020-10-27 22:53:37.846 DEBUG loaders - load_file: Loading JSON file: /Users/dmoton/opt/anaconda3/lib/python3.7/site-packages/botocore/data/redshift/2012-12-01/service-2.json
2020-10-27 22:53:37.868 DEBUG hooks - _emit: Event creating-client-class.redshift: calling handler <function add_generate_presigned_url at 0x10c7e5e60>
2020-10-27 22:53:37.928 DEBUG endpoint - create_endpoint: Setting redshift timeout as (60, 60)
2020-10-27 22:53:37.931 DEBUG client - _register_legacy_retries: Registering retry handlers for service: redshift
2020-10-27 22:53:37.932 DEBUG factory - load_from_definition: Loading s3:Bucket
2020-10-27 22:53:37.934 DEBUG model - _load_name_with_category: Renaming Bucket attribute name
2020-10-27 22:53:37.948 DEBUG hooks - _emit: Event creating-resource-class.s3.Bucket: calling handler <function lazy_call.<locals>._handler at 0x11bc40050>
2020-10-27 22:53:37.949 DEBUG factory - load_from_definition: Loading s3:Bucket
2020-10-27 22:53:37.955 DEBUG model - _load_name_with_category: Renaming Bucket attribute name
2020-10-27 22:53:37.956 DEBUG hooks - _emit: Event creating-resource-class.s3.Bucket: calling handler <function lazy_call.<locals>._handler at 0x11bc40050>
2020-10-27 22:53:37.956 DEBUG hooks - _emit: Event before-parameter-build.iam.GetRole: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:37.957 DEBUG hooks - _emit: Event before-call.iam.GetRole: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:37.957 DEBUG endpoint - make_request: Making request for OperationModel(name=GetRole) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'GetRole', 'Version': '2010-05-08', 'RoleName': 'myRedshiftRole'}, 'url': 'https://iam.amazonaws.com/', 'context': {'client_region': 'aws-global', 'client_config': <botocore.config.Config object at 0x11d42be50>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:37.957 DEBUG hooks - _emit: Event request-created.iam.GetRole: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d42bd50>>
2020-10-27 22:53:37.958 DEBUG hooks - _emit: Event choose-signer.iam.GetRole: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:37.958 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:37.958 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:iam.amazonaws.com
x-amz-date:20201028T025337Z

content-type;host;x-amz-date
132abeea69e768f56c00f0bb26ed83d4ccc24861aab9e2f83323a2340c5458f6
2020-10-27 22:53:37.959 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025337Z
20201028/us-east-1/iam/aws4_request
5fadb0089e61fed643ef14bab318c8d0c52481d03cebcb5a48016064f213f708
2020-10-27 22:53:37.959 DEBUG auth - add_auth: Signature:
86d4b76ab4d8ab60c8d1159ccdc7d951c959f4d7afbf989d72c282d0f1267663
2020-10-27 22:53:37.959 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://iam.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025337Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=86d4b76ab4d8ab60c8d1159ccdc7d951c959f4d7afbf989d72c282d0f1267663', 'Content-Length': '57'}>
2020-10-27 22:53:37.960 DEBUG connectionpool - _new_conn: Starting new HTTPS connection (1): iam.amazonaws.com:443
2020-10-27 22:53:38.223 DEBUG connectionpool - _make_request: https://iam.amazonaws.com:443 "POST / HTTP/1.1" 200 972
2020-10-27 22:53:38.224 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'acd829ac-2d0a-4d5d-a446-176aa69749a1', 'Content-Type': 'text/xml', 'Content-Length': '972', 'Date': 'Wed, 28 Oct 2020 02:42:22 GMT'}
2020-10-27 22:53:38.224 DEBUG parsers - parse: Response body:
b'<GetRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">\n  <GetRoleResult>\n    <Role>\n      <Path>/</Path>\n      <AssumeRolePolicyDocument>%7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22%2A%22%2C%22Service%22%3A%22s3.amazonaws.com%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole%22%7D%5D%7D</AssumeRolePolicyDocument>\n      <MaxSessionDuration>3600</MaxSessionDuration>\n      <RoleId>AROA5NVJNZGMLZCLMQD34</RoleId>\n      <RoleLastUsed>\n        <LastUsedDate>2020-10-27T23:38:41Z</LastUsedDate>\n        <Region>us-west-2</Region>\n      </RoleLastUsed>\n      <RoleName>myRedshiftRole</RoleName>\n      <Description/>\n      <Arn>arn:aws:iam::922699549080:role/myRedshiftRole</Arn>\n      <CreateDate>2020-10-23T23:57:53Z</CreateDate>\n    </Role>\n  </GetRoleResult>\n  <ResponseMetadata>\n    <RequestId>acd829ac-2d0a-4d5d-a446-176aa69749a1</RequestId>\n  </ResponseMetadata>\n</GetRoleResponse>\n'
2020-10-27 22:53:38.228 DEBUG hooks - _emit: Event needs-retry.iam.GetRole: calling handler <botocore.retryhandler.RetryHandler object at 0x11d44d690>
2020-10-27 22:53:38.228 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:38.228 DEBUG hooks - _emit: Event after-call.iam.GetRole: calling handler <function json_decode_policies at 0x10c842050>
2020-10-27 22:53:38.230 DEBUG hooks - _emit: Event before-parameter-build.iam.AttachRolePolicy: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:38.230 DEBUG hooks - _emit: Event before-call.iam.AttachRolePolicy: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:38.230 DEBUG endpoint - make_request: Making request for OperationModel(name=AttachRolePolicy) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'AttachRolePolicy', 'Version': '2010-05-08', 'RoleName': 'myRedshiftRole', 'PolicyArn': 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'}, 'url': 'https://iam.amazonaws.com/', 'context': {'client_region': 'aws-global', 'client_config': <botocore.config.Config object at 0x11d42be50>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:38.231 DEBUG hooks - _emit: Event request-created.iam.AttachRolePolicy: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d42bd50>>
2020-10-27 22:53:38.231 DEBUG hooks - _emit: Event choose-signer.iam.AttachRolePolicy: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:38.232 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:38.232 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:iam.amazonaws.com
x-amz-date:20201028T025338Z

content-type;host;x-amz-date
a1a2a8341ec83995b25c9ba432d3834c266d3723a3c632062615a578449fa9fd
2020-10-27 22:53:38.232 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025338Z
20201028/us-east-1/iam/aws4_request
2d687d38d33b19c69e3040846f707667975f56c33167d815336db80e0e6b2548
2020-10-27 22:53:38.232 DEBUG auth - add_auth: Signature:
6f4f9a5375d22e862b839cd66f7cce7cdc9bf149df77a390c3f5c59c91687f0c
2020-10-27 22:53:38.233 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://iam.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025338Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=6f4f9a5375d22e862b839cd66f7cce7cdc9bf149df77a390c3f5c59c91687f0c', 'Content-Length': '135'}>
2020-10-27 22:53:38.317 DEBUG connectionpool - _make_request: https://iam.amazonaws.com:443 "POST / HTTP/1.1" 200 212
2020-10-27 22:53:38.318 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'a977a1fa-ee66-4b0f-934d-f7a32b2fe525', 'Content-Type': 'text/xml', 'Content-Length': '212', 'Date': 'Wed, 28 Oct 2020 02:42:22 GMT'}
2020-10-27 22:53:38.318 DEBUG parsers - parse: Response body:
b'<AttachRolePolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">\n  <ResponseMetadata>\n    <RequestId>a977a1fa-ee66-4b0f-934d-f7a32b2fe525</RequestId>\n  </ResponseMetadata>\n</AttachRolePolicyResponse>\n'
2020-10-27 22:53:38.320 DEBUG hooks - _emit: Event needs-retry.iam.AttachRolePolicy: calling handler <botocore.retryhandler.RetryHandler object at 0x11d44d690>
2020-10-27 22:53:38.320 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:38.320 DEBUG hooks - _emit: Event after-call.iam.AttachRolePolicy: calling handler <function json_decode_policies at 0x10c842050>
2020-10-27 22:53:38.322 DEBUG hooks - _emit: Event before-parameter-build.iam.GetRole: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:38.323 DEBUG hooks - _emit: Event before-call.iam.GetRole: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:38.323 DEBUG endpoint - make_request: Making request for OperationModel(name=GetRole) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'GetRole', 'Version': '2010-05-08', 'RoleName': 'myRedshiftRole'}, 'url': 'https://iam.amazonaws.com/', 'context': {'client_region': 'aws-global', 'client_config': <botocore.config.Config object at 0x11d42be50>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:38.324 DEBUG hooks - _emit: Event request-created.iam.GetRole: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d42bd50>>
2020-10-27 22:53:38.324 DEBUG hooks - _emit: Event choose-signer.iam.GetRole: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:38.325 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:38.325 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:iam.amazonaws.com
x-amz-date:20201028T025338Z

content-type;host;x-amz-date
132abeea69e768f56c00f0bb26ed83d4ccc24861aab9e2f83323a2340c5458f6
2020-10-27 22:53:38.325 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025338Z
20201028/us-east-1/iam/aws4_request
4acfd83ac68ad479d303665fbcd9329a8e6a1179d68a692510d5f0b907b44bcd
2020-10-27 22:53:38.325 DEBUG auth - add_auth: Signature:
36502e1ac8638019324ca1e8ad6bdc5c87dcc809170f34836064ff48a4e9aef8
2020-10-27 22:53:38.325 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://iam.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025338Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=36502e1ac8638019324ca1e8ad6bdc5c87dcc809170f34836064ff48a4e9aef8', 'Content-Length': '57'}>
2020-10-27 22:53:38.390 DEBUG connectionpool - _make_request: https://iam.amazonaws.com:443 "POST / HTTP/1.1" 200 972
2020-10-27 22:53:38.391 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '40a081f7-df23-409e-8041-f8e8da43cef0', 'Content-Type': 'text/xml', 'Content-Length': '972', 'Date': 'Wed, 28 Oct 2020 02:42:23 GMT'}
2020-10-27 22:53:38.391 DEBUG parsers - parse: Response body:
b'<GetRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">\n  <GetRoleResult>\n    <Role>\n      <Path>/</Path>\n      <AssumeRolePolicyDocument>%7B%22Version%22%3A%222012-10-17%22%2C%22Statement%22%3A%5B%7B%22Effect%22%3A%22Allow%22%2C%22Principal%22%3A%7B%22AWS%22%3A%22%2A%22%2C%22Service%22%3A%22s3.amazonaws.com%22%7D%2C%22Action%22%3A%22sts%3AAssumeRole%22%7D%5D%7D</AssumeRolePolicyDocument>\n      <MaxSessionDuration>3600</MaxSessionDuration>\n      <RoleId>AROA5NVJNZGMLZCLMQD34</RoleId>\n      <RoleLastUsed>\n        <LastUsedDate>2020-10-27T23:38:41Z</LastUsedDate>\n        <Region>us-west-2</Region>\n      </RoleLastUsed>\n      <RoleName>myRedshiftRole</RoleName>\n      <Description/>\n      <Arn>arn:aws:iam::922699549080:role/myRedshiftRole</Arn>\n      <CreateDate>2020-10-23T23:57:53Z</CreateDate>\n    </Role>\n  </GetRoleResult>\n  <ResponseMetadata>\n    <RequestId>40a081f7-df23-409e-8041-f8e8da43cef0</RequestId>\n  </ResponseMetadata>\n</GetRoleResponse>\n'
2020-10-27 22:53:38.393 DEBUG hooks - _emit: Event needs-retry.iam.GetRole: calling handler <botocore.retryhandler.RetryHandler object at 0x11d44d690>
2020-10-27 22:53:38.393 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:38.393 DEBUG hooks - _emit: Event after-call.iam.GetRole: calling handler <function json_decode_policies at 0x10c842050>
2020-10-27 22:53:38.394 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:38.395 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:38.395 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:38.395 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:53:38.396 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:38.396 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:38.397 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025338Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:53:38.397 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025338Z
20201028/us-east-2/redshift/aws4_request
6427f89e00a80b0d353948e7eacc944eaa2ce1857d15ef99143b2397aa743e58
2020-10-27 22:53:38.397 DEBUG auth - add_auth: Signature:
7d99df64404b252d4e2e9c6932d6ca850e1adfd4bc765dbae4489192f2343387
2020-10-27 22:53:38.397 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025338Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=7d99df64404b252d4e2e9c6932d6ca850e1adfd4bc765dbae4489192f2343387', 'Content-Length': '71'}>
2020-10-27 22:53:38.398 DEBUG connectionpool - _new_conn: Starting new HTTPS connection (1): redshift.us-east-2.amazonaws.com:443
2020-10-27 22:53:38.598 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 404 280
2020-10-27 22:53:38.599 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'f03377e4-bf0f-43f1-89b0-c6a120efb2a7', 'Content-Type': 'text/xml', 'Content-Length': '280', 'Date': 'Wed, 28 Oct 2020 02:42:23 GMT'}
2020-10-27 22:53:38.599 DEBUG parsers - parse: Response body:
b'<ErrorResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <Error>\n    <Type>Sender</Type>\n    <Code>ClusterNotFound</Code>\n    <Message>Cluster awscluster not found.</Message>\n  </Error>\n  <RequestId>f03377e4-bf0f-43f1-89b0-c6a120efb2a7</RequestId>\n</ErrorResponse>\n'
2020-10-27 22:53:38.604 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'f03377e4-bf0f-43f1-89b0-c6a120efb2a7', 'Content-Type': 'text/xml', 'Content-Length': '280', 'Date': 'Wed, 28 Oct 2020 02:42:23 GMT'}
2020-10-27 22:53:38.605 DEBUG parsers - parse: Response body:
b'<ErrorResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <Error>\n    <Type>Sender</Type>\n    <Code>ClusterNotFound</Code>\n    <Message>Cluster awscluster not found.</Message>\n  </Error>\n  <RequestId>f03377e4-bf0f-43f1-89b0-c6a120efb2a7</RequestId>\n</ErrorResponse>\n'
2020-10-27 22:53:38.605 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:53:38.605 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:38.608 DEBUG hooks - _emit: Event before-parameter-build.redshift.CreateCluster: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:38.610 DEBUG hooks - _emit: Event before-call.redshift.CreateCluster: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:38.610 DEBUG endpoint - make_request: Making request for OperationModel(name=CreateCluster) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'CreateCluster', 'Version': '2012-12-01', 'ClusterType': 'single-node', 'NodeType': 'dc2.large', 'DBName': 'dev', 'ClusterIdentifier': 'awscluster', 'MasterUsername': 'awsuser', 'MasterUserPassword': 'DENDproject3', 'IamRoles.IamRoleArn.1': 'arn:aws:iam::922699549080:role/myRedshiftRole'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:38.610 DEBUG hooks - _emit: Event request-created.redshift.CreateCluster: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:53:38.611 DEBUG hooks - _emit: Event choose-signer.redshift.CreateCluster: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:38.612 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:38.612 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025338Z

content-type;host;x-amz-date
d30f05e1dbbb6d196708e9d6e13a43f34012f14a5534f96f7068254db79e2db3
2020-10-27 22:53:38.612 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025338Z
20201028/us-east-2/redshift/aws4_request
72cecc38f9df019f71b3b391ebceb711dbd267da418088270268f3d8a330ae79
2020-10-27 22:53:38.612 DEBUG auth - add_auth: Signature:
1a5a3136bb610089088bf7abdc1067aef549502fef9aa43cbe584eb2ea9a6c64
2020-10-27 22:53:38.612 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025338Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=1a5a3136bb610089088bf7abdc1067aef549502fef9aa43cbe584eb2ea9a6c64', 'Content-Length': '257'}>
2020-10-27 22:53:39.790 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 2221
2020-10-27 22:53:39.792 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'bf2acb09-51ee-4e43-a90a-9c1f776e2d8f', 'Content-Type': 'text/xml', 'Content-Length': '2221', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:42:24 GMT'}
2020-10-27 22:53:39.792 DEBUG parsers - parse: Response body:
b'<CreateClusterResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <CreateClusterResult>\n    <Cluster>\n      <AllowVersionUpgrade>true</AllowVersionUpgrade>\n      <ClusterIdentifier>awscluster</ClusterIdentifier>\n      <NumberOfNodes>1</NumberOfNodes>\n      <ClusterVersion>1.0</ClusterVersion>\n      <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n      <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n      <VpcId>vpc-047966a7282741705</VpcId>\n      <PubliclyAccessible>true</PubliclyAccessible>\n      <MasterUsername>awsuser</MasterUsername>\n      <DBName>dev</DBName>\n      <EnhancedVpcRouting>false</EnhancedVpcRouting>\n      <IamRoles>\n        <ClusterIamRole>\n          <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n          <ApplyStatus>adding</ApplyStatus>\n        </ClusterIamRole>\n      </IamRoles>\n      <ClusterSecurityGroups/>\n      <NodeType>dc2.large</NodeType>\n      <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n      <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n      <DeferredMaintenanceWindows/>\n      <Tags/>\n      <VpcSecurityGroups>\n        <VpcSecurityGroup>\n          <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n          <Status>active</Status>\n        </VpcSecurityGroup>\n      </VpcSecurityGroups>\n      <ClusterParameterGroups>\n        <ClusterParameterGroup>\n          <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n          <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n        </ClusterParameterGroup>\n      </ClusterParameterGroups>\n      <Encrypted>false</Encrypted>\n      <MaintenanceTrackName>current</MaintenanceTrackName>\n      <PendingModifiedValues>\n        <MasterUserPassword>****</MasterUserPassword>\n      </PendingModifiedValues>\n      <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n      <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n      <ClusterStatus>creating</ClusterStatus>\n    </Cluster>\n  </CreateClusterResult>\n  <ResponseMetadata>\n    <RequestId>bf2acb09-51ee-4e43-a90a-9c1f776e2d8f</RequestId>\n  </ResponseMetadata>\n</CreateClusterResponse>\n'
2020-10-27 22:53:39.797 DEBUG hooks - _emit: Event needs-retry.redshift.CreateCluster: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:53:39.798 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:39.799 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:39.800 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:39.800 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:39.801 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:53:39.801 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:39.801 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:39.801 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025339Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:53:39.802 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025339Z
20201028/us-east-2/redshift/aws4_request
a6cc9be7419bf92dd00bba0144cc9125a049779dffe3d3cb054f9a9bb1752ce7
2020-10-27 22:53:39.802 DEBUG auth - add_auth: Signature:
2b10f7f47caf405fdd7f6466316ab5aa4f07a1fa49d5ded8aa1f1a3be2914f38
2020-10-27 22:53:39.802 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025339Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=2b10f7f47caf405fdd7f6466316ab5aa4f07a1fa49d5ded8aa1f1a3be2914f38', 'Content-Length': '71'}>
2020-10-27 22:53:39.943 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 2586
2020-10-27 22:53:39.944 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '0ffac95f-1b08-4439-b445-95fe187d2445', 'Content-Type': 'text/xml', 'Content-Length': '2586', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:42:24 GMT'}
2020-10-27 22:53:39.944 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>adding</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes/>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>0ffac95f-1b08-4439-b445-95fe187d2445</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:53:39.947 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:53:39.947 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:53:39.947 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:53:39.948 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:53:39.948 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:53:39.949 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:53:39.950 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:53:39.951 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:53:39.951 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025339Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:53:39.951 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025339Z
20201028/us-east-2/redshift/aws4_request
a6cc9be7419bf92dd00bba0144cc9125a049779dffe3d3cb054f9a9bb1752ce7
2020-10-27 22:53:39.952 DEBUG auth - add_auth: Signature:
2b10f7f47caf405fdd7f6466316ab5aa4f07a1fa49d5ded8aa1f1a3be2914f38
2020-10-27 22:53:39.952 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025339Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=2b10f7f47caf405fdd7f6466316ab5aa4f07a1fa49d5ded8aa1f1a3be2914f38', 'Content-Length': '71'}>
2020-10-27 22:53:40.072 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 2586
2020-10-27 22:53:40.072 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '0c73ad4c-2f36-435e-b7de-6b09a843e501', 'Content-Type': 'text/xml', 'Content-Length': '2586', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:42:24 GMT'}
2020-10-27 22:53:40.073 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>adding</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes/>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>0c73ad4c-2f36-435e-b7de-6b09a843e501</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:53:40.075 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:53:40.076 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:54:10.085 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:54:10.091 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:54:10.092 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:54:10.093 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:54:10.094 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:54:10.097 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:54:10.097 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025410Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:54:10.097 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025410Z
20201028/us-east-2/redshift/aws4_request
30ad72ab13854427af8af578122e78ed2bc86fc45c177b1c9975c9645e898d4e
2020-10-27 22:54:10.097 DEBUG auth - add_auth: Signature:
f5f726e0984cd3ebf5ab85110cbcac9ea91b2464c52a17c09da0708c313b6817
2020-10-27 22:54:10.098 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025410Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=f5f726e0984cd3ebf5ab85110cbcac9ea91b2464c52a17c09da0708c313b6817', 'Content-Length': '71'}>
2020-10-27 22:54:10.101 DEBUG connectionpool - _get_conn: Resetting dropped connection: redshift.us-east-2.amazonaws.com
2020-10-27 22:54:10.378 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3370
2020-10-27 22:54:10.382 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'ff3daebb-f79b-442a-9582-aa9919a0c9b7', 'Content-Type': 'text/xml', 'Content-Length': '3370', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:42:54 GMT'}
2020-10-27 22:54:10.382 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>ff3daebb-f79b-442a-9582-aa9919a0c9b7</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:54:10.387 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:54:10.388 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:54:40.394 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:54:40.401 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:54:40.402 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:54:40.404 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:54:40.405 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:54:40.409 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:54:40.409 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025440Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:54:40.409 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025440Z
20201028/us-east-2/redshift/aws4_request
eed7325aa52cc815296e03d260a7c2931246de45b082bb126ab8f0077ddacee8
2020-10-27 22:54:40.410 DEBUG auth - add_auth: Signature:
02573b62bba1d90ac37efeb0394daadb2c26fe8a684f2d94c46d7339421412ff
2020-10-27 22:54:40.410 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025440Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=02573b62bba1d90ac37efeb0394daadb2c26fe8a684f2d94c46d7339421412ff', 'Content-Length': '71'}>
2020-10-27 22:54:40.413 DEBUG connectionpool - _get_conn: Resetting dropped connection: redshift.us-east-2.amazonaws.com
2020-10-27 22:54:40.713 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3370
2020-10-27 22:54:40.716 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '345a97e8-72e4-4d84-9053-800de21a3068', 'Content-Type': 'text/xml', 'Content-Length': '3370', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:43:24 GMT'}
2020-10-27 22:54:40.716 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>345a97e8-72e4-4d84-9053-800de21a3068</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:54:40.739 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:54:40.740 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:55:10.748 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:55:10.750 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:55:10.753 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:55:10.753 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:55:10.754 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:55:10.754 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:55:10.755 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025510Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:55:10.755 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025510Z
20201028/us-east-2/redshift/aws4_request
cc83254f2bee1c7250a90ced90db0f3ab133d436e46943bfd809b845d4e02787
2020-10-27 22:55:10.755 DEBUG auth - add_auth: Signature:
e33605f37c2dc544f7fd7c622e662694fd8bdce353f19bd3722ab231938de6c3
2020-10-27 22:55:10.755 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025510Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=e33605f37c2dc544f7fd7c622e662694fd8bdce353f19bd3722ab231938de6c3', 'Content-Length': '71'}>
2020-10-27 22:55:10.756 DEBUG connectionpool - _get_conn: Resetting dropped connection: redshift.us-east-2.amazonaws.com
2020-10-27 22:55:11.001 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3370
2020-10-27 22:55:11.002 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '067be6cc-c63b-4a31-b958-01a11a222749', 'Content-Type': 'text/xml', 'Content-Length': '3370', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:43:55 GMT'}
2020-10-27 22:55:11.002 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>067be6cc-c63b-4a31-b958-01a11a222749</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:55:11.004 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:55:11.004 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:55:41.014 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:55:41.021 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:55:41.021 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:55:41.023 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:55:41.023 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:55:41.026 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:55:41.026 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025541Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:55:41.026 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025541Z
20201028/us-east-2/redshift/aws4_request
c0ea3fb9eec32a21ae35144add40793e3177f619423e6448fa1a5ad67c301de6
2020-10-27 22:55:41.027 DEBUG auth - add_auth: Signature:
2a614c33dd25a88cf9ad63aa20fce7c0c2a81913896f6bbab9d3535d8c72fe99
2020-10-27 22:55:41.027 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025541Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=2a614c33dd25a88cf9ad63aa20fce7c0c2a81913896f6bbab9d3535d8c72fe99', 'Content-Length': '71'}>
2020-10-27 22:55:41.031 DEBUG connectionpool - _get_conn: Resetting dropped connection: redshift.us-east-2.amazonaws.com
2020-10-27 22:55:41.241 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3370
2020-10-27 22:55:41.244 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': '47bdb184-6a13-4701-ac4c-dd82c838d5a9', 'Content-Type': 'text/xml', 'Content-Length': '3370', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:44:25 GMT'}
2020-10-27 22:55:41.244 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Modifying</ClusterAvailabilityStatus>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues>\n          <MasterUserPassword>****</MasterUserPassword>\n        </PendingModifiedValues>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>creating</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>47bdb184-6a13-4701-ac4c-dd82c838d5a9</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:55:41.247 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:55:41.247 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:56:11.249 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:56:11.251 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:56:11.251 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:56:11.252 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:56:11.252 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:56:11.252 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:56:11.253 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025611Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:56:11.253 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025611Z
20201028/us-east-2/redshift/aws4_request
cb395d8eedf514c89f1d05744b5d50e9d8de8e43bd6000e6e39f7ba04cdc0c40
2020-10-27 22:56:11.253 DEBUG auth - add_auth: Signature:
6aa1ebfa72f344a4624e850dd334dc838092dc08b599d8ec3b934522909ba9ba
2020-10-27 22:56:11.253 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025611Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=6aa1ebfa72f344a4624e850dd334dc838092dc08b599d8ec3b934522909ba9ba', 'Content-Length': '71'}>
2020-10-27 22:56:11.254 DEBUG connectionpool - _get_conn: Resetting dropped connection: redshift.us-east-2.amazonaws.com
2020-10-27 22:56:11.463 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3508
2020-10-27 22:56:11.464 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'f5c9be61-dffc-4847-b188-bca2b911d26a', 'Content-Type': 'text/xml', 'Content-Length': '3508', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:44:55 GMT'}
2020-10-27 22:56:11.465 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>\n        <Endpoint>\n          <Address>awscluster.cxfxmvoetkw1.us-east-2.redshift.amazonaws.com</Address>\n          <Port>5439</Port>\n        </Endpoint>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <ClusterCreateTime>2020-10-28T02:44:31.487Z</ClusterCreateTime>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues/>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>available</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>f5c9be61-dffc-4847-b188-bca2b911d26a</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:56:11.468 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:56:11.468 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:56:11.469 DEBUG hooks - _emit: Event before-parameter-build.redshift.DescribeClusters: calling handler <function generate_idempotent_uuid at 0x10c83f4d0>
2020-10-27 22:56:11.469 DEBUG hooks - _emit: Event before-call.redshift.DescribeClusters: calling handler <function inject_api_version_header_if_needed at 0x10c842d40>
2020-10-27 22:56:11.469 DEBUG endpoint - make_request: Making request for OperationModel(name=DescribeClusters) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0'}, 'body': {'Action': 'DescribeClusters', 'Version': '2012-12-01', 'ClusterIdentifier': 'awscluster'}, 'url': 'https://redshift.us-east-2.amazonaws.com/', 'context': {'client_region': 'us-east-2', 'client_config': <botocore.config.Config object at 0x11d60b210>, 'has_streaming_input': False, 'auth_type': None}}
2020-10-27 22:56:11.469 DEBUG hooks - _emit: Event request-created.redshift.DescribeClusters: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x11d60b1d0>>
2020-10-27 22:56:11.470 DEBUG hooks - _emit: Event choose-signer.redshift.DescribeClusters: calling handler <function set_operation_specific_signer at 0x10c83d9e0>
2020-10-27 22:56:11.470 DEBUG auth - add_auth: Calculating signature using v4 auth.
2020-10-27 22:56:11.470 DEBUG auth - add_auth: CanonicalRequest:
POST
/

content-type:application/x-www-form-urlencoded; charset=utf-8
host:redshift.us-east-2.amazonaws.com
x-amz-date:20201028T025611Z

content-type;host;x-amz-date
709941464356f7b9c6b794a3f82af2e76df0da5ee2a5b3f6d7058ddcfac71b1d
2020-10-27 22:56:11.470 DEBUG auth - add_auth: StringToSign:
AWS4-HMAC-SHA256
20201028T025611Z
20201028/us-east-2/redshift/aws4_request
cb395d8eedf514c89f1d05744b5d50e9d8de8e43bd6000e6e39f7ba04cdc0c40
2020-10-27 22:56:11.470 DEBUG auth - add_auth: Signature:
6aa1ebfa72f344a4624e850dd334dc838092dc08b599d8ec3b934522909ba9ba
2020-10-27 22:56:11.471 DEBUG endpoint - _do_get_response: Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://redshift.us-east-2.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'Boto3/1.16.0 Python/3.7.6 Darwin/19.4.0 Botocore/1.19.0', 'X-Amz-Date': b'20201028T025611Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA5NVJNZGMOIAEPI42/20201028/us-east-2/redshift/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=6aa1ebfa72f344a4624e850dd334dc838092dc08b599d8ec3b934522909ba9ba', 'Content-Length': '71'}>
2020-10-27 22:56:11.554 DEBUG connectionpool - _make_request: https://redshift.us-east-2.amazonaws.com:443 "POST / HTTP/1.1" 200 3508
2020-10-27 22:56:11.555 DEBUG parsers - parse: Response headers: {'x-amzn-RequestId': 'fa348e93-d2c2-40c5-88f6-db9f3e541653', 'Content-Type': 'text/xml', 'Content-Length': '3508', 'vary': 'accept-encoding', 'Date': 'Wed, 28 Oct 2020 02:44:55 GMT'}
2020-10-27 22:56:11.555 DEBUG parsers - parse: Response body:
b'<DescribeClustersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">\n  <DescribeClustersResult>\n    <Clusters>\n      <Cluster>\n        <AllowVersionUpgrade>true</AllowVersionUpgrade>\n        <ClusterIdentifier>awscluster</ClusterIdentifier>\n        <ClusterRevisionNumber>19884</ClusterRevisionNumber>\n        <NumberOfNodes>1</NumberOfNodes>\n        <ClusterPublicKey>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCdkCC7RJ7azT1Pjvnz/47dGSoXIDL9PmrciYz/7sXA/e00CpjvhMbp+CdthIoMOh+wh63CVC614DjFl8eJQ0BgW/v644BxZpkjTa+k1JWvJh3w3IiETcqOlKdbocYKR5V5N6tR+9Vd0LxwY8R88m5RzgGBGtlFnhBGy74a+Hygafh8i7auhonyHyPsb0JYgYurYtjF60OGJmRkfjaSZ7F4VrTf3r1NiCs2b8NdL2NBSeTwdKVwc4Zwmu+ZDqRKky56/enTLDmRAFZ83EdqPesnDnvSj3LAteO3Rtv/0LwjtaRd6v0XeAoEyD7pl37Y4LNIn7d2UWAWgqK+fghW7g8f Amazon-Redshift\n</ClusterPublicKey>\n        <AvailabilityZone>us-east-2a</AvailabilityZone>\n        <ClusterVersion>1.0</ClusterVersion>\n        <ManualSnapshotRetentionPeriod>-1</ManualSnapshotRetentionPeriod>\n        <ClusterAvailabilityStatus>Available</ClusterAvailabilityStatus>\n        <Endpoint>\n          <Address>awscluster.cxfxmvoetkw1.us-east-2.redshift.amazonaws.com</Address>\n          <Port>5439</Port>\n        </Endpoint>\n        <VpcId>vpc-047966a7282741705</VpcId>\n        <PubliclyAccessible>true</PubliclyAccessible>\n        <ClusterCreateTime>2020-10-28T02:44:31.487Z</ClusterCreateTime>\n        <MasterUsername>awsuser</MasterUsername>\n        <DBName>dev</DBName>\n        <EnhancedVpcRouting>false</EnhancedVpcRouting>\n        <IamRoles>\n          <ClusterIamRole>\n            <IamRoleArn>arn:aws:iam::922699549080:role/myRedshiftRole</IamRoleArn>\n            <ApplyStatus>in-sync</ApplyStatus>\n          </ClusterIamRole>\n        </IamRoles>\n        <ClusterNamespaceArn>arn:aws:redshift:us-east-2:922699549080:namespace:5ca9e12f-eaa3-4255-9a16-97a9c100d60e</ClusterNamespaceArn>\n        <ClusterSecurityGroups/>\n        <NodeType>dc2.large</NodeType>\n        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>\n        <NextMaintenanceWindowStartTime>2020-10-28T05:00:00Z</NextMaintenanceWindowStartTime>\n        <DeferredMaintenanceWindows/>\n        <Tags/>\n        <VpcSecurityGroups>\n          <VpcSecurityGroup>\n            <VpcSecurityGroupId>sg-099b541cb940d810b</VpcSecurityGroupId>\n            <Status>active</Status>\n          </VpcSecurityGroup>\n        </VpcSecurityGroups>\n        <ClusterParameterGroups>\n          <ClusterParameterGroup>\n            <ParameterGroupName>default.redshift-1.0</ParameterGroupName>\n            <ParameterApplyStatus>in-sync</ParameterApplyStatus>\n          </ClusterParameterGroup>\n        </ClusterParameterGroups>\n        <Encrypted>false</Encrypted>\n        <ClusterNodes>\n          <member>\n            <PrivateIPAddress>172.31.3.144</PrivateIPAddress>\n            <NodeRole>SHARED</NodeRole>\n            <PublicIPAddress>18.224.0.97</PublicIPAddress>\n          </member>\n        </ClusterNodes>\n        <MaintenanceTrackName>current</MaintenanceTrackName>\n        <PendingModifiedValues/>\n        <PreferredMaintenanceWindow>wed:05:00-wed:05:30</PreferredMaintenanceWindow>\n        <AutomatedSnapshotRetentionPeriod>1</AutomatedSnapshotRetentionPeriod>\n        <ClusterStatus>available</ClusterStatus>\n        <AzDisasterRecoveryStatus>disabled</AzDisasterRecoveryStatus>\n      </Cluster>\n    </Clusters>\n  </DescribeClustersResult>\n  <ResponseMetadata>\n    <RequestId>fa348e93-d2c2-40c5-88f6-db9f3e541653</RequestId>\n  </ResponseMetadata>\n</DescribeClustersResponse>\n'
2020-10-27 22:56:11.557 DEBUG hooks - _emit: Event needs-retry.redshift.DescribeClusters: calling handler <botocore.retryhandler.RetryHandler object at 0x11d60b9d0>
2020-10-27 22:56:11.558 DEBUG retryhandler - __call__: No retry needed.
2020-10-27 22:56:11.558 DEBUG <ipython-input-11-cfefe9eebbfa> - create_cluster: Done initializing AWS resources
