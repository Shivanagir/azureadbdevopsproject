// Databricks notebook source
dbutils.widgets.text("aad_client_id", "")
dbutils.widgets.text("tenant_id", "")
dbutils.widgets.text("dlsGen2Source", "")

// COMMAND ----------

val tenantId = dbutils.widgets.get("tenant_id")
val aad_client_id = dbutils.widgets.get("aad_client_id")
val dlsGen2Source = dbutils.widgets.get("dlsGen2Source")
val endpoint = "https://login.microsoftonline.com/" + tenantId + "/oauth2/token"
val scopeName = "my-training-scope-v2"
val secretName = "dlsaccesstoken"
val client_secret = dbutils.secrets.get(scope = scopeName, key = secretName)
val configs = Map(
  "fs.azure.account.auth.type" -> "OAuth",
  "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id" -> aad_client_id,
  "fs.azure.account.oauth2.client.secret" -> client_secret,
  "fs.azure.account.oauth2.client.endpoint" -> endpoint)

// COMMAND ----------

import scala.util.control.Breaks._
 
val availableMounts = dbutils.fs.mounts()
val mountPath = "/mnt/data"
var isExist: Boolean = false
 
breakable {
  for(mount <- availableMounts) {
    if(mount.mountPoint == mountPath) {
      isExist = true
      
      break
    }
  }
}
 
if(!isExist) {
  dbutils.fs.mount(
    source = dlsGen2Source,
    mountPoint = mountPath,
    extraConfigs = configs)
  
  println("Volume Mounting Successfully Completed!")
  
  dbutils.notebook.exit("Success")
} else {
  println("Volume Mounting Already Exist!")
  dbutils.notebook.exit("Failure")
}
