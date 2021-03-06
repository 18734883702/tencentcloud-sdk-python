# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param DvAuthMethod: 验证方式：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。
        :type DvAuthMethod: str
        :param DomainName: 域名。
        :type DomainName: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param PackageType: 证书类型，目前仅支持类型2。2 = TrustAsia TLS RSA CA。
        :type PackageType: str
        :param ContactEmail: 邮箱。
        :type ContactEmail: str
        :param ContactPhone: 手机。
        :type ContactPhone: str
        :param ValidityPeriod: 有效期，默认12个月，目前仅支持12个月。
        :type ValidityPeriod: str
        :param CsrEncryptAlgo: 加密算法，仅支持 RSA。
        :type CsrEncryptAlgo: str
        :param CsrKeyParameter: 密钥对参数，仅支持2048。
        :type CsrKeyParameter: str
        :param CsrKeyPassword: CSR 的加密密码。
        :type CsrKeyPassword: str
        :param Alias: 备注名称。
        :type Alias: str
        :param OldCertificateId: 原证书 ID，用于重新申请。
        :type OldCertificateId: str
        """
        self.DvAuthMethod = None
        self.DomainName = None
        self.ProjectId = None
        self.PackageType = None
        self.ContactEmail = None
        self.ContactPhone = None
        self.ValidityPeriod = None
        self.CsrEncryptAlgo = None
        self.CsrKeyParameter = None
        self.CsrKeyPassword = None
        self.Alias = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.DvAuthMethod = params.get("DvAuthMethod")
        self.DomainName = params.get("DomainName")
        self.ProjectId = params.get("ProjectId")
        self.PackageType = params.get("PackageType")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPhone = params.get("ContactPhone")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self.CsrKeyParameter = params.get("CsrKeyParameter")
        self.CsrKeyPassword = params.get("CsrKeyPassword")
        self.Alias = params.get("Alias")
        self.OldCertificateId = params.get("OldCertificateId")


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 取消订单成功的证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CertificateExtra(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 数组下，key为CertificateExtra 的内容。

    """

    def __init__(self):
        """
        :param DomainNumber: 证书可配置域名数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNumber: str
        :param OriginCertificateId: 原始证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertificateId: str
        :param ReplacedBy: 重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedBy: str
        :param ReplacedFor: 重颁发证书新 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedFor: str
        :param RenewOrder: 新订单证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewOrder: str
        """
        self.DomainNumber = None
        self.OriginCertificateId = None
        self.ReplacedBy = None
        self.ReplacedFor = None
        self.RenewOrder = None


    def _deserialize(self, params):
        self.DomainNumber = params.get("DomainNumber")
        self.OriginCertificateId = params.get("OriginCertificateId")
        self.ReplacedBy = params.get("ReplacedBy")
        self.ReplacedFor = params.get("ReplacedFor")
        self.RenewOrder = params.get("RenewOrder")


class Certificates(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 的内容。

    """

    def __init__(self):
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = Symantec 增强型企业版（EV Pro）， 4 = Symantec 增强型（EV）， 5 = Symantec 企业型专业版（OV Pro）， 6 = Symantec 企业型（OV）， 7 = Symantec 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 主域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 状态值 0：审核中，1：已通过，2：审核失败，3：已过期，4：已添加云解析记录，5：OV/EV 证书，待提交资料，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期，单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 状态名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param ProjectInfo: 项目信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param BoundResource: 关联的云资源，暂不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundResource: list of str
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.PackageType = None
        self.CertificateType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.CertificateExtra = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.CertificateId = None
        self.SubjectAltName = None
        self.PackageTypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.ProjectInfo = None
        self.BoundResource = None
        self.Deployable = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.PackageType = params.get("PackageType")
        self.CertificateType = params.get("CertificateType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.CertificateId = params.get("CertificateId")
        self.SubjectAltName = params.get("SubjectAltName")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = ProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.BoundResource = params.get("BoundResource")
        self.Deployable = params.get("Deployable")


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation返回参数结构体

    """

    def __init__(self):
        """
        :param OrderId: 亚信订单号。
        :type OrderId: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param DeleteResult: 删除结果。
        :type DeleteResult: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = Symantec 增强型企业版（EV Pro）， 4 = Symantec 增强型（EV）， 5 = Symantec 企业型专业版（OV Pro）， 6 = Symantec 企业型（OV）， 7 = Symantec 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期：单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param CertificatePrivateKey: 证书私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePrivateKey: str
        :param CertificatePublicKey: 证书公钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePublicKey: str
        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param TypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 证书包含的多个域名（包含主域名）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.CertificatePrivateKey = None
        self.CertificatePublicKey = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.TypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.SubmittedData = None
        self.RenewAble = None
        self.Deployable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.RenewAble = params.get("RenewAble")
        self.Deployable = params.get("Deployable")
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 请求日志数量，默认为20。
        :type Limit: int
        :param StartTime: 开始时间，默认15天前。
        :type StartTime: str
        :param EndTime: 结束时间，默认现在时间。
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs返回参数结构体

    """

    def __init__(self):
        """
        :param AllTotal: 当前查询条件日志总数。
        :type AllTotal: int
        :param TotalCount: 本次请求返回的日志数量。
        :type TotalCount: int
        :param OperateLogs: 证书操作日志列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateLogs: list of OperationLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllTotal = None
        self.TotalCount = None
        self.OperateLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self.OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self.OperateLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = Symantec 增强型企业版（EV Pro）， 4 = Symantec 增强型（EV）， 5 = Symantec 企业型专业版（OV Pro）， 6 = Symantec 企业型（OV）， 7 = Symantec 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 证书办法者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.PackageTypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.SubmittedData = None
        self.Deployable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.Deployable = params.get("Deployable")
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认20。
        :type Limit: int
        :param SearchKey: 搜索关键词，可搜索证书 ID、备注名称、域名。例如： a8xHcaIs。
        :type SearchKey: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param ExpirationSort: 按到期时间排序：DESC = 降序， ASC = 升序。
        :type ExpirationSort: str
        :param CertificateStatus: 证书状态。
        :type CertificateStatus: list of int non-negative
        :param Deployable: 是否可部署，可选值：1 = 可部署，0 =  不可部署。
        :type Deployable: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertificateType = None
        self.ProjectId = None
        self.ExpirationSort = None
        self.CertificateStatus = None
        self.Deployable = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertificateType = params.get("CertificateType")
        self.ProjectId = params.get("ProjectId")
        self.ExpirationSort = params.get("ExpirationSort")
        self.CertificateStatus = params.get("CertificateStatus")
        self.Deployable = params.get("Deployable")


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Certificates: 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificates: list of Certificates
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Certificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self.Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self.Certificates.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param Content: ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param ContentType: MIME 类型：application/zip = ZIP 压缩文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ContentType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ContentType = params.get("ContentType")
        self.RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 DvAuthDetail 的内容。

    """

    def __init__(self):
        """
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthKeySubDomain: DV 认证子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKeySubDomain: str
        :param DvAuths: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuths: list of DvAuths
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthKeySubDomain = None
        self.DvAuths = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self.DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self.DvAuths.append(obj)


class DvAuths(AbstractModel):
    """获取证书列表（Certificate）返回参数键为 DvAuths 的内容。

    """

    def __init__(self):
        """
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthSubDomain: DV 认证子域名，
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthSubDomain: str
        :param DvAuthVerifyType: DV 认证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthVerifyType: str
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthSubDomain = None
        self.DvAuthVerifyType = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthSubDomain = params.get("DvAuthSubDomain")
        self.DvAuthVerifyType = params.get("DvAuthVerifyType")


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param Alias: 备注名称。
        :type Alias: str
        """
        self.CertificateId = None
        self.Alias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Alias = params.get("Alias")


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 修改成功的证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateIdList: 需要修改所属项目的证书 ID 集合，最多100个证书。
        :type CertificateIdList: list of str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        """
        self.CertificateIdList = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificateIdList = params.get("CertificateIdList")
        self.ProjectId = params.get("ProjectId")


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessCertificates: 修改所属项目成功的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCertificates: list of str
        :param FailCertificates: 修改所属项目失败的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCertificates: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCertificates = None
        self.FailCertificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCertificates = params.get("SuccessCertificates")
        self.FailCertificates = params.get("FailCertificates")
        self.RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """证书操作日志。

    """

    def __init__(self):
        """
        :param Action: 操作证书动作。
        :type Action: str
        :param CreatedOn: 操作时间。
        :type CreatedOn: str
        """
        self.Action = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CreatedOn = params.get("CreatedOn")


class ProjectInfo(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 下，key为 ProjectInfo 的内容。

    """

    def __init__(self):
        """
        :param ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectCreatorUin: 项目创建用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreatorUin: int
        :param ProjectCreateTime: 项目创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreateTime: str
        :param ProjectResume: 项目信息简述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectResume: str
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        """
        self.ProjectName = None
        self.ProjectCreatorUin = None
        self.ProjectCreateTime = None
        self.ProjectResume = None
        self.OwnerUin = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectCreatorUin = params.get("ProjectCreatorUin")
        self.ProjectCreateTime = params.get("ProjectCreateTime")
        self.ProjectResume = params.get("ProjectResume")
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param ValidType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。
        :type ValidType: str
        :param CsrType: 类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。
        :type CsrType: str
        :param CsrContent: CSR 内容。
        :type CsrContent: str
        :param CsrkeyPassword: KEY 密码。
        :type CsrkeyPassword: str
        """
        self.CertificateId = None
        self.ValidType = None
        self.CsrType = None
        self.CsrContent = None
        self.CsrkeyPassword = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ValidType = params.get("ValidType")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CsrkeyPassword = params.get("CsrkeyPassword")


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param CsrType: CSR 生成方式：online = 在线生成, parse = 手动上传。
        :type CsrType: str
        :param CsrContent: 上传的 CSR 内容。
        :type CsrContent: str
        :param CertificateDomain: 绑定证书的域名。
        :type CertificateDomain: str
        :param DomainList: 上传的域名数组（多域名证书可以上传）。
        :type DomainList: list of str
        :param KeyPassword: 私钥密码。
        :type KeyPassword: str
        :param OrganizationName: 公司名称。
        :type OrganizationName: str
        :param OrganizationDivision: 部门名称。
        :type OrganizationDivision: str
        :param OrganizationAddress: 公司详细地址。
        :type OrganizationAddress: str
        :param OrganizationCountry: 国家名称，如中国：CN 。
        :type OrganizationCountry: str
        :param OrganizationCity: 公司所在城市。
        :type OrganizationCity: str
        :param OrganizationRegion: 公司所在省份。
        :type OrganizationRegion: str
        :param PostalCode: 公司邮编。
        :type PostalCode: str
        :param PhoneAreaCode: 公司座机区号。
        :type PhoneAreaCode: str
        :param PhoneNumber: 公司座机号码。
        :type PhoneNumber: str
        :param VerifyType: 证书验证方式。
        :type VerifyType: str
        :param AdminFirstName: 管理人姓。
        :type AdminFirstName: str
        :param AdminLastName: 管理人名。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理人手机号码。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理人邮箱地址。
        :type AdminEmail: str
        :param AdminPosition: 管理人职位。
        :type AdminPosition: str
        :param ContactFirstName: 联系人姓。
        :type ContactFirstName: str
        :param ContactLastName: 联系人名。
        :type ContactLastName: str
        :param ContactEmail: 联系人邮箱地址。
        :type ContactEmail: str
        :param ContactNumber: 联系人手机号码。
        :type ContactNumber: str
        :param ContactPosition: 联系人职位。
        :type ContactPosition: str
        """
        self.CertificateId = None
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.VerifyType = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactEmail = None
        self.ContactNumber = None
        self.ContactPosition = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.VerifyType = params.get("VerifyType")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactPosition = params.get("ContactPosition")


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 SubmittedData 的内容。

    """

    def __init__(self):
        """
        :param CsrType: CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrType: str
        :param CsrContent: CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrContent: str
        :param CertificateDomain: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateDomain: str
        :param DomainList: DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param KeyPassword: 私钥密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPassword: str
        :param OrganizationName: 企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param OrganizationDivision: 部门。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationDivision: str
        :param OrganizationAddress: 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationAddress: str
        :param OrganizationCountry: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCountry: str
        :param OrganizationCity: 市。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCity: str
        :param OrganizationRegion: 省。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationRegion: str
        :param PostalCode: 邮政编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param PhoneAreaCode: 座机区号。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneAreaCode: str
        :param PhoneNumber: 座机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param AdminFirstName: 管理员名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminFirstName: str
        :param AdminLastName: 管理员姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminEmail: str
        :param AdminPosition: 管理员职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPosition: str
        :param ContactFirstName: 联系人名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactFirstName: str
        :param ContactLastName: 联系人姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactLastName: str
        :param ContactNumber: 联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactNumber: str
        :param ContactEmail: 联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactEmail: str
        :param ContactPosition: 联系人职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactPosition: str
        :param VerifyType: 验证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        """
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactNumber = None
        self.ContactEmail = None
        self.ContactPosition = None
        self.VerifyType = None


    def _deserialize(self, params):
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPosition = params.get("ContactPosition")
        self.VerifyType = params.get("VerifyType")


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificatePublicKey: 证书公钥。
        :type CertificatePublicKey: str
        :param CertificatePrivateKey: 私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。
        :type CertificatePrivateKey: str
        :param CertificateType: 证书类型，默认 SVR。CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param Alias: 备注名称。
        :type Alias: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        """
        self.CertificatePublicKey = None
        self.CertificatePrivateKey = None
        self.CertificateType = None
        self.Alias = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificateType = params.get("CertificateType")
        self.Alias = params.get("Alias")
        self.ProjectId = params.get("ProjectId")


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate返回参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")