https://github.com/google-coral/libedgetpu/blob/master/tflite/edgetpu_manager_direct.cc

```C++
EdgeTpuManagerDirect::EnumerateEdgeTpuInternal() const {
  std::vector<edgetpu::EdgeTpuManager::DeviceEnumerationRecord> result;

  auto factory = api::DriverFactory::GetOrCreate();
  if (!factory) {
    VLOG(1) << "Failed to create driver factory.";
    return result;
  }

  auto devices = factory->Enumerate();

  for (const auto& device : devices) {
    edgetpu::DeviceType device_type =
        static_cast<edgetpu::DeviceType>(DeviceTypeExtended::kUnknown);
    if (device.chip == api::Chip::kBeagle) {
      switch (device.type) {
        case api::Device::Type::PCI:
          device_type = edgetpu::DeviceType::kApexPci;
          break;
        case api::Device::Type::USB:
          device_type = edgetpu::DeviceType::kApexUsb;
          break;
        case api::Device::Type::REFERENCE:
          device_type = static_cast<edgetpu::DeviceType>(
              DeviceTypeExtended::kApexReference);
          break;
        default:
          VLOG(7) << "Skipping unrecognized device type: "
                  << static_cast<int>(device.type);
          continue;
      }
    } else {
      VLOG(7) << "Skipping unrecognized Edge TPU type: "
              << static_cast<int>(device.chip);
      continue;
    }

    result.push_back(edgetpu::EdgeTpuManager::DeviceEnumerationRecord{
        device_type, device.path});
  }
  return result;
}
```

![](https://github.com/system-software-lab/nrf20/blob/main/device/devboard.JPG?raw=true)
![](https://github.com/system-software-lab/nrf20/blob/main/device/usbaccelerator.JPG?raw=true)

![](https://github.com/system-software-lab/nrf20/blob/main/device/nvidia%20gpu%20codename.JPG?raw=true)
https://nouveau.freedesktop.org/CodeNames.html

https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/common_runtime/gpu/gpu_device.cc
![](https://github.com/pinguin-der-bellt/ssl-2020/blob/main/device/jetson_gpu2.JPG?raw=true)

```python
Status BaseGPUDeviceFactory::CreateGPUDevice(
    const SessionOptions& options, const string& name_prefix, TfGpuId tf_gpu_id,
    int64 memory_limit, const DeviceLocality& dev_locality,
    std::vector<std::unique_ptr<Device>>* devices) {
  CHECK_GE(tf_gpu_id.value(), 0);
  const string device_name =
      strings::StrCat(name_prefix, "/device:GPU:", tf_gpu_id.value());
  DeviceIdUtil::CheckValidTfDeviceId(DEVICE_GPU, GPUMachineManager(),
                                     tf_gpu_id);
  PlatformGpuId platform_gpu_id;
  TF_RETURN_IF_ERROR(
      GpuIdManager::TfToPlatformGpuId(tf_gpu_id, &platform_gpu_id));
  int numa_node = dev_locality.numa_node();

  se::Platform* gpu_manager = GPUMachineManager();
  auto desc_status = gpu_manager->DescriptionForDevice(platform_gpu_id.value());
  if (!desc_status.ok()) {
    return desc_status.status();
  }
  auto desc = desc_status.ConsumeValueOrDie();
  GPUProcessState* process_state = GPUProcessState::singleton();
  Allocator* gpu_allocator = process_state->GetGPUAllocator(
      options.config.gpu_options(), tf_gpu_id, memory_limit);
  if (gpu_allocator == nullptr) {
    return errors::Internal("Failed to get memory allocator for TF GPU ",
                            tf_gpu_id.value(), " with ", memory_limit,
                            " bytes of memory.");
  }
  absl::optional<AllocatorStats> stats = gpu_allocator->GetStats();
  if (!stats) {
    return errors::Internal("No allocator statistics");
  }
  // 'memory_limit' is the required memory size, but if the allocator with
  // given tf_gpu_id was created before, we'll use it instead of creating a
  // new one (as TF gpu device is a shared resource), in which case the actual
  // memory limit represented by 'stats.bytes_limit' used by that allocator
  // may be different (which should be an error).
  //
  // TODO(laigd): report error if memory_limit doesn't match
  // stats->bytes_limit.
  int64 bytes_limit = stats->bytes_limit ? *stats->bytes_limit : 0;
  std::unique_ptr<BaseGPUDevice> gpu_device = CreateGPUDevice(
      options, device_name, static_cast<Bytes>(bytes_limit), dev_locality,
      tf_gpu_id, GetShortDeviceDescription(platform_gpu_id, *desc),
      gpu_allocator, ProcessState::singleton()->GetCPUAllocator(numa_node));
  LOG(INFO) << "Created TensorFlow device (" << device_name << " with "
            << (bytes_limit >> 20) << " MB memory) -> physical GPU ("
            << GetShortDeviceDescription(platform_gpu_id, *desc) << ")";
  TF_RETURN_IF_ERROR(gpu_device->Init(options));
  devices->push_back(std::move(gpu_device));

  return Status::OK();
}
```
