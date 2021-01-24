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
