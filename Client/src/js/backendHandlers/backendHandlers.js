import axios from 'axios';

// TODO: Move configuration to backend

const backendConfig = {
    "protocol": "http",
    "hostname": "localhost",
    "port": 8081,
    "routes": {
        "analyzer": {
            "path": "juggling/analyzer",
            "params": ["siteswap"]
        },
        "transactions": {
            "path": "juggling/transactions",
            "params": ["siteswap_1", "siteswap_2"]
        }
    }
}

axios.defaults.port = backendConfig.port;

const baseBackendUrl = backendConfig.protocol
    + '://' + backendConfig.hostname
    + ':' + backendConfig.port;

const getFullUrlPath = (serviceName) => {
    return baseBackendUrl + "/" + backendConfig.routes[serviceName].path;
}

const parsePatternJson = (data) => {
    data.beatmap = JSON.parse(data.beatmap);
    data.problems = JSON.parse(data.problems);
    return data;
}

const createQuery = (serviceName, siteswaps) => {
    let query = {};
    const params = backendConfig.routes[serviceName].params;
    for (var i = 0; i < params.length; i++) {
        query[params[i]] = siteswaps[i];
    }
    return query;
}

export async function defaultBackendRequest(serviceName, siteswaps) {
    const path = getFullUrlPath(serviceName);
    const query = createQuery(serviceName, siteswaps);
    const response = await axios.post(path, query).catch((err) => {
        console.log("uhkhkuh");
        return false;
    });
    return await parsePatternJson(response.data);
};