// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: ttf_sensor_api.proto
#ifndef GRPC_ttf_5fsensor_5fapi_2eproto__INCLUDED
#define GRPC_ttf_5fsensor_5fapi_2eproto__INCLUDED

#include "ttf_sensor_api.pb.h"

#include <functional>
#include <grpcpp/generic/async_generic_service.h>
#include <grpcpp/support/async_stream.h>
#include <grpcpp/support/async_unary_call.h>
#include <grpcpp/support/client_callback.h>
#include <grpcpp/client_context.h>
#include <grpcpp/completion_queue.h>
#include <grpcpp/support/message_allocator.h>
#include <grpcpp/support/method_handler.h>
#include <grpcpp/impl/proto_utils.h>
#include <grpcpp/impl/rpc_method.h>
#include <grpcpp/support/server_callback.h>
#include <grpcpp/impl/server_callback_handlers.h>
#include <grpcpp/server_context.h>
#include <grpcpp/impl/service_type.h>
#include <grpcpp/support/status.h>
#include <grpcpp/support/stub_options.h>
#include <grpcpp/support/sync_stream.h>

namespace ttf_sensor_api {

// The DigitalSensor service definition
class TTFSensorService final {
 public:
  static constexpr char const* service_full_name() {
    return "ttf_sensor_api.TTFSensorService";
  }
  class StubInterface {
   public:
    virtual ~StubInterface() {}
    // Get sensor status
    virtual ::grpc::Status GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::ttf_sensor_api::MeasureResponse* response) = 0;
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>> AsyncGetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>>(AsyncGetMeasureRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>> PrepareAsyncGetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>>(PrepareAsyncGetMeasureRaw(context, request, cq));
    }
    class async_interface {
     public:
      virtual ~async_interface() {}
      // Get sensor status
      virtual void GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response, std::function<void(::grpc::Status)>) = 0;
      virtual void GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response, ::grpc::ClientUnaryReactor* reactor) = 0;
    };
    typedef class async_interface experimental_async_interface;
    virtual class async_interface* async() { return nullptr; }
    class async_interface* experimental_async() { return async(); }
   private:
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>* AsyncGetMeasureRaw(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) = 0;
    virtual ::grpc::ClientAsyncResponseReaderInterface< ::ttf_sensor_api::MeasureResponse>* PrepareAsyncGetMeasureRaw(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) = 0;
  };
  class Stub final : public StubInterface {
   public:
    Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());
    ::grpc::Status GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::ttf_sensor_api::MeasureResponse* response) override;
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>> AsyncGetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>>(AsyncGetMeasureRaw(context, request, cq));
    }
    std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>> PrepareAsyncGetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) {
      return std::unique_ptr< ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>>(PrepareAsyncGetMeasureRaw(context, request, cq));
    }
    class async final :
      public StubInterface::async_interface {
     public:
      void GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response, std::function<void(::grpc::Status)>) override;
      void GetMeasure(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response, ::grpc::ClientUnaryReactor* reactor) override;
     private:
      friend class Stub;
      explicit async(Stub* stub): stub_(stub) { }
      Stub* stub() { return stub_; }
      Stub* stub_;
    };
    class async* async() override { return &async_stub_; }

   private:
    std::shared_ptr< ::grpc::ChannelInterface> channel_;
    class async async_stub_{this};
    ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>* AsyncGetMeasureRaw(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) override;
    ::grpc::ClientAsyncResponseReader< ::ttf_sensor_api::MeasureResponse>* PrepareAsyncGetMeasureRaw(::grpc::ClientContext* context, const ::ttf_sensor_api::Measure& request, ::grpc::CompletionQueue* cq) override;
    const ::grpc::internal::RpcMethod rpcmethod_GetMeasure_;
  };
  static std::unique_ptr<Stub> NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options = ::grpc::StubOptions());

  class Service : public ::grpc::Service {
   public:
    Service();
    virtual ~Service();
    // Get sensor status
    virtual ::grpc::Status GetMeasure(::grpc::ServerContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response);
  };
  template <class BaseClass>
  class WithAsyncMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithAsyncMethod_GetMeasure() {
      ::grpc::Service::MarkMethodAsync(0);
    }
    ~WithAsyncMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestGetMeasure(::grpc::ServerContext* context, ::ttf_sensor_api::Measure* request, ::grpc::ServerAsyncResponseWriter< ::ttf_sensor_api::MeasureResponse>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(0, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  typedef WithAsyncMethod_GetMeasure<Service > AsyncService;
  template <class BaseClass>
  class WithCallbackMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithCallbackMethod_GetMeasure() {
      ::grpc::Service::MarkMethodCallback(0,
          new ::grpc::internal::CallbackUnaryHandler< ::ttf_sensor_api::Measure, ::ttf_sensor_api::MeasureResponse>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::ttf_sensor_api::Measure* request, ::ttf_sensor_api::MeasureResponse* response) { return this->GetMeasure(context, request, response); }));}
    void SetMessageAllocatorFor_GetMeasure(
        ::grpc::MessageAllocator< ::ttf_sensor_api::Measure, ::ttf_sensor_api::MeasureResponse>* allocator) {
      ::grpc::internal::MethodHandler* const handler = ::grpc::Service::GetHandler(0);
      static_cast<::grpc::internal::CallbackUnaryHandler< ::ttf_sensor_api::Measure, ::ttf_sensor_api::MeasureResponse>*>(handler)
              ->SetMessageAllocator(allocator);
    }
    ~WithCallbackMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* GetMeasure(
      ::grpc::CallbackServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/)  { return nullptr; }
  };
  typedef WithCallbackMethod_GetMeasure<Service > CallbackService;
  typedef CallbackService ExperimentalCallbackService;
  template <class BaseClass>
  class WithGenericMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithGenericMethod_GetMeasure() {
      ::grpc::Service::MarkMethodGeneric(0);
    }
    ~WithGenericMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
  };
  template <class BaseClass>
  class WithRawMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawMethod_GetMeasure() {
      ::grpc::Service::MarkMethodRaw(0);
    }
    ~WithRawMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    void RequestGetMeasure(::grpc::ServerContext* context, ::grpc::ByteBuffer* request, ::grpc::ServerAsyncResponseWriter< ::grpc::ByteBuffer>* response, ::grpc::CompletionQueue* new_call_cq, ::grpc::ServerCompletionQueue* notification_cq, void *tag) {
      ::grpc::Service::RequestAsyncUnary(0, context, request, response, new_call_cq, notification_cq, tag);
    }
  };
  template <class BaseClass>
  class WithRawCallbackMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithRawCallbackMethod_GetMeasure() {
      ::grpc::Service::MarkMethodRawCallback(0,
          new ::grpc::internal::CallbackUnaryHandler< ::grpc::ByteBuffer, ::grpc::ByteBuffer>(
            [this](
                   ::grpc::CallbackServerContext* context, const ::grpc::ByteBuffer* request, ::grpc::ByteBuffer* response) { return this->GetMeasure(context, request, response); }));
    }
    ~WithRawCallbackMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable synchronous version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    virtual ::grpc::ServerUnaryReactor* GetMeasure(
      ::grpc::CallbackServerContext* /*context*/, const ::grpc::ByteBuffer* /*request*/, ::grpc::ByteBuffer* /*response*/)  { return nullptr; }
  };
  template <class BaseClass>
  class WithStreamedUnaryMethod_GetMeasure : public BaseClass {
   private:
    void BaseClassMustBeDerivedFromService(const Service* /*service*/) {}
   public:
    WithStreamedUnaryMethod_GetMeasure() {
      ::grpc::Service::MarkMethodStreamed(0,
        new ::grpc::internal::StreamedUnaryHandler<
          ::ttf_sensor_api::Measure, ::ttf_sensor_api::MeasureResponse>(
            [this](::grpc::ServerContext* context,
                   ::grpc::ServerUnaryStreamer<
                     ::ttf_sensor_api::Measure, ::ttf_sensor_api::MeasureResponse>* streamer) {
                       return this->StreamedGetMeasure(context,
                         streamer);
                  }));
    }
    ~WithStreamedUnaryMethod_GetMeasure() override {
      BaseClassMustBeDerivedFromService(this);
    }
    // disable regular version of this method
    ::grpc::Status GetMeasure(::grpc::ServerContext* /*context*/, const ::ttf_sensor_api::Measure* /*request*/, ::ttf_sensor_api::MeasureResponse* /*response*/) override {
      abort();
      return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
    }
    // replace default version of method with streamed unary
    virtual ::grpc::Status StreamedGetMeasure(::grpc::ServerContext* context, ::grpc::ServerUnaryStreamer< ::ttf_sensor_api::Measure,::ttf_sensor_api::MeasureResponse>* server_unary_streamer) = 0;
  };
  typedef WithStreamedUnaryMethod_GetMeasure<Service > StreamedUnaryService;
  typedef Service SplitStreamedService;
  typedef WithStreamedUnaryMethod_GetMeasure<Service > StreamedService;
};

}  // namespace ttf_sensor_api


#endif  // GRPC_ttf_5fsensor_5fapi_2eproto__INCLUDED