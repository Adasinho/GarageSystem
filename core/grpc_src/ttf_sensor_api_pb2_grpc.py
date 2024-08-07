# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import ttf_sensor_api_pb2 as ttf__sensor__api__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in ttf_sensor_api_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TTFSensorStub(object):
    """The DigitalSensor service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMeasure = channel.unary_unary(
                '/ttf_sensor_api.TTFSensor/GetMeasure',
                request_serializer=ttf__sensor__api__pb2.MeasureRequest.SerializeToString,
                response_deserializer=ttf__sensor__api__pb2.MeasureResponse.FromString,
                _registered_method=True)


class TTFSensorServicer(object):
    """The DigitalSensor service definition
    """

    def GetMeasure(self, request, context):
        """Get sensor status
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TTFSensorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMeasure': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasure,
                    request_deserializer=ttf__sensor__api__pb2.MeasureRequest.FromString,
                    response_serializer=ttf__sensor__api__pb2.MeasureResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ttf_sensor_api.TTFSensor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ttf_sensor_api.TTFSensor', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TTFSensor(object):
    """The DigitalSensor service definition
    """

    @staticmethod
    def GetMeasure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ttf_sensor_api.TTFSensor/GetMeasure',
            ttf__sensor__api__pb2.MeasureRequest.SerializeToString,
            ttf__sensor__api__pb2.MeasureResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
