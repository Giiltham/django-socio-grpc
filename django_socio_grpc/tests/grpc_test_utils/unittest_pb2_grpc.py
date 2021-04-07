# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from django_socio_grpc.tests.grpc_test_utils import unittest_pb2 as django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class UnitTestControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/unittest.UnitTestController/List',
                request_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestListRequest.SerializeToString,
                response_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                )
        self.Create = channel.unary_unary(
                '/unittest.UnitTestController/Create',
                request_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
                response_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/unittest.UnitTestController/Retrieve',
                request_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestRetrieveRequest.SerializeToString,
                response_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                )
        self.Update = channel.unary_unary(
                '/unittest.UnitTestController/Update',
                request_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
                response_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/unittest.UnitTestController/Destroy',
                request_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UnitTestControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UnitTestControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestListRequest.FromString,
                    response_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                    response_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestRetrieveRequest.FromString,
                    response_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                    response_serializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unittest.UnitTestController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UnitTestController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/unittest.UnitTestController/List',
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestListRequest.SerializeToString,
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unittest.UnitTestController/Create',
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unittest.UnitTestController/Retrieve',
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTestRetrieveRequest.SerializeToString,
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unittest.UnitTestController/Update',
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unittest.UnitTestController/Destroy',
            django__socio__grpc_dot_tests_dot_grpc__test__utils_dot_unittest__pb2.UnitTest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
