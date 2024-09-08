# from model.geonode_proxy_server import GeonodeProxyServers, Datum, AnonymityLevel, Protocol
# from datetime import datetime
#
#
# class JsonParser:
#
#     @classmethod
#     def parse_datum(cls, datum_json) -> Datum:
#         return Datum(
#             id=datum_json["_id"],
#             ip=datum_json["ip"],
#             anonymity_level=AnonymityLevel(datum_json["anonymityLevel"]),
#             asn=datum_json.get("asn"),
#             city=datum_json["city"],
#             country=datum_json["country"],
#             created_at=datetime.fromisoformat(datum_json["created_at"].replace("Z", "+00:00")),
#             google=datum_json["google"],
#             isp=datum_json["isp"],
#             last_checked=datum_json["lastChecked"],
#             latency=datum_json["latency"],
#             org=datum_json.get("org"),
#             port=int(datum_json["port"]),
#             protocols=[Protocol(protocol) for protocol in datum_json["protocols"]],
#             region=datum_json.get("region"),
#             response_time=datum_json["responseTime"],
#             speed=datum_json["speed"],
#             updated_at=datetime.fromisoformat(datum_json["updated_at"].replace("Z", "+00:00")),
#             working_percent=datum_json.get("workingPercent"),
#             up_time=datum_json["upTime"],
#             up_time_success_count=datum_json["upTimeSuccessCount"],
#             up_time_try_count=datum_json["upTimeTryCount"],
#         )
#
#     @classmethod
#     def parse_geonode_proxy_servers(cls, json_data) -> GeonodeProxyServers:
#         data = [cls.parse_datum(datum) for datum in json_data["data"]]
#         return GeonodeProxyServers(
#             data=data,
#             total=json_data["total"],
#             page=json_data["page"],
#             limit=json_data["limit"]
#         )
