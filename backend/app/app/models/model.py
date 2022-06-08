from typing import Optional

from sqlmodel import Field, SQLModel



class KubeBurner(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str
    platform: str
    ocp_version: str
    k8s_version: str
    master_nodes_type: str
    worker_nodes_type: str
    infra_nodes_type: str
    workload_nodes_type: str
    master_nodes_count: int
    worker_nodes_count: int
    infra_nodes_count: int
    workload_nodes_count: int
    total_nodes: int
    sdn_type: str
    timestamp: int
    end_date: int
    workload: str
    ocp_nightly_version: str
    podLatencyQuantilesMeasurement_ContainersReady_avg_P99: float
    podLatencyQuantilesMeasurement_Initialized_avg_P99: float
    podLatencyQuantilesMeasurement_PodScheduled_avg_P99: float
    podLatencyMeasurement_avg: float
    APIRequestRate_avg: float
    containerMemory_Masters_avg: float
    containerCPU_Masters_avg: float
    readOnlyAPICallsLatency_avg: float
    containerCPU_AggregatedWorkers_avg: float
    containerMemory_AggregatedWorkers_avg: float
    containerMemory_Infra_avg: float
    mutatingAPICallsLatency_avg: float
    containerCPU_Infra_avg: float
    containerNetworkSetupLatency_avg: float
    nodeCPU_Masters_avg: float
    nodeCPU_Infra_avg: float
    nodeCPU_AggregatedWorkers_avg: float
    ninetyNinthEtcdRoundTripTimeSeconds_avg: float
    podStatusCount_avg: float
    nodeStatus_avg: float
    ninetyNinthEtcdDiskBackendCommitDurationSeconds_avg: float
    ninetyNinthEtcdDiskWalFsyncDurationSeconds_avg: float
    nodeMemoryAvailable_Infra_avg: float
    nodeMemoryAvailable_Masters_avg: float
    nodeMemoryTotal_Infra_avg: float
    nodeMemoryTotal_Masters_avg: float
    nodeMemoryUtilization_Masters_avg: float
    namespaceCount_avg: float
    etcdLeaderChangesRate_avg: float
    nodeMemoryAvailable_AggregatedWorkers_avg: float
    serviceSyncLatency_avg: float
    schedulingThroughput_avg: float
    podLatencyQuantilesMeasurement_avg: float
    clusterVersion_avg: float
    configmapCount_avg: float
    deploymentCount_avg: float
    etcdVersion_avg: float
    nodeMemoryTotal_AggregatedWorkers_avg: float
    secretCount_avg: float
    serviceCount_avg: float